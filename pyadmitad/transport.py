import requests
from base64 import b64encode
import simplejson
import urllib
import urlparse
import uuid
from pyadmitad.constants import *
from pyadmitad.exceptions import *


def prepare_request_data(data=None, headers=None, method='GET',
                         timeout=None, ssl_verify=False):
    if headers is None:
        headers = {}
    kwargs = {}
    if timeout is None:
        timeout = DEFAULT_REQUEST_TIMEOUT
    kwargs['timeout'] = timeout
    if method == 'POST':
        kwargs['data'] = data
    if method == 'GET':
        kwargs['params'] = data
    kwargs['headers'] = headers
    kwargs['allow_redirects'] = True
    kwargs['verify'] = ssl_verify
    return kwargs


def api_request(url, data=None, headers=None, method='GET',
                timeout=None, ssl_verify=False):
    kwargs = prepare_request_data(
        data=data, headers=headers, method=method,
        timeout=timeout, ssl_verify=ssl_verify)
    status_code = 500
    content = {}
    try:
        response = requests.request(method, url, **kwargs)
        status_code = response.status_code
        response.raise_for_status()
        content = response.json()
        return content
    except requests.HTTPError as err:
        raise HttpException(status_code, content, err)
    except requests.RequestException as err:
        raise ConnectionException(err)
    except simplejson.JSONDecodeError as err:
        raise JsonException(err)


def api_post_request(url, **kwargs):
    kwargs['method'] = "POST"
    return api_request(url, **kwargs)


def api_get_request(url, **kwargs):
    kwargs['method'] = "GET"
    return api_request(url, **kwargs)


def build_authorization_headers(access_token):
    return {'Authorization': "Bearer %s" % access_token}


def build_headers(access_token, user_agent=None):
    headers = build_authorization_headers(access_token)
    headers['Connection'] = 'Keep-Alive'
    if user_agent:
        headers['User-Agent'] = user_agent
    return headers


def prepare_api_url(url, **kwargs):
    if kwargs is None:
        kwargs = {}
    # set default language
    language = kwargs.get('language')
    if not language:
        kwargs['language'] = DEFAULT_LANGUAGE
    return url % kwargs


def oauth_password_authorization(data):
    """
    OAuth2 password authorization
    Used to get access_token with the user's password and username
    """
    client_id = data['client_id']
    client_secret = data['client_secret']
    language = data.get('language', DEFAULT_LANGUAGE)
    params = {
        'grant_type': 'password',
        'client_id': client_id,
        'username': data['username'],
        'password': data['password'],
        'scope': data['scopes']
    }
    credentials = b64encode("%s:%s" % (client_id, client_secret))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic %s' % credentials
    }
    return api_post_request(
        prepare_api_url(TOKEN_URL, language=language),
        data=params, headers=headers)


def oauth_client_authorization(data):
    """
    OAuth2 client authorization.
    Used to get access_token with the oauth client credentials
    """
    client_id = data['client_id']
    client_secret = data['client_secret']
    language = data.get('language', DEFAULT_LANGUAGE)
    params = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'scope': data['scopes']
    }
    credentials = b64encode("%s:%s" % (client_id, client_secret))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic %s' % credentials
    }
    return api_post_request(
        prepare_api_url(TOKEN_URL, language=language),
        data=params, headers=headers)


class OAuthServerAuthorisation(object):

    def __init__(self, data):
        self.client_id = data['client_id']
        self.client_secret = data['client_secret']
        self.scopes = data['scopes']
        self.redirect_uri = data.get('redirect_uri')
        self.language = data.get('language', DEFAULT_LANGUAGE)
        self.state = None

    def get_authorize_url(self):
        """
        Get an url that client should be redirected to pass
        the authentication
        """
        self.state = uuid.uuid4().get_hex()
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
            'state': self.state,
            'scope': self.scopes,
            'redirect_uri': self.redirect_uri
        }
        return "%s?%s" % (
            prepare_api_url(AUTHORIZE_URL, language=self.language),
            urllib.urlencode(params))

    def get_access_token(self, url):
        """
        Get access token request.
        The URL parameter is a URL to which the client was redirected
        after authentication
        """
        url_params = dict(urlparse.parse_qsl(urlparse.urlparse(url).query))
        state = url_params.get('state')
        if not state or state != self.state:
            raise ApiException('Wrong or absent the state parameter.')
        if 'error' in url_params:
            raise ApiException(url_params['error'])
        if 'code' not in url_params:
            raise ApiException(
                'Invalid response. The authorization code is absent.')
        # go to get access token
        params = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': url_params['code'],
            'redirect_uri': self.redirect_uri
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = api_post_request(
            prepare_api_url(TOKEN_URL, language=self.language),
            data=params, headers=headers)
        if 'access_token' not in response:
            raise ApiException('Invalid response. The access_token is absent.')
        return response


class HttpTransportPagination(object):

    DEFAULT_LIMIT = 20
    DEFAULT_OFFSET = 0

    def __init__(self, **kwargs):
        self.offset = self._get_pagination_offset(**kwargs)
        self.limit = self._get_pagination_limit(**kwargs)

    @staticmethod
    def _check_pagination_value(value, maximum=None, minimum=None):
        try:
            value = int(value)
        except (ValueError, TypeError):
            return
        if value < 0:
            return
        if maximum is not None and value > maximum:
            return
        if minimum is not None and value < minimum:
            return
        return value

    def _get_pagination_limit(self, **kwargs):
        if 'limit' in kwargs:
            limit = self._check_pagination_value(
                kwargs['limit'], MAX_PAGINATION_LIMIT, 1)
            if limit is not None:
                return limit
        return self.DEFAULT_LIMIT

    def _get_pagination_offset(self, **kwargs):
        if 'offset' in kwargs:
            offset = self._check_pagination_value(kwargs['offset'])
            if offset is not None:
                return offset
        return self.DEFAULT_OFFSET

    def to_value(self):
        return {'limit': self.limit, 'offset': self.offset}


class HttpTransportOrdering(object):

    ORDER_PARAMETER = 'order_by'

    def __init__(self, **kwargs):
        allowed_ordering = kwargs.get('allowed_ordering', ())
        ordering = str(kwargs.get(self.ORDER_PARAMETER, ''))
        suffix = ''
        if ordering:
            if ordering.startswith('-'):
                suffix = '-'
                ordering = ordering[1:]
            if ordering not in allowed_ordering:
                ordering = None
        self.ordering = ordering
        self.suffix = suffix

    def to_value(self):
        if self.ordering:
            return {self.ORDER_PARAMETER: '%s%s' % (self.suffix, self.ordering)}
        return {}


class HttpTransport(object):

    def __init__(self, access_token, method=None, user_agent=None):
        self._headers = build_headers(access_token, user_agent=user_agent)
        self._method = method or 'GET'
        self._supported_methods = ('GET', 'POST')
        self._supported_languages = ('ru', 'en', 'de', 'pl')
        self._data = None
        self._url = None
        self._language = None

    def set_url(self, url, **kwargs):
        language = kwargs.get('language')
        if language:
            self.set_language(language)
        if self._language:
            kwargs['language'] = self._language
        self._url = prepare_api_url(url, **kwargs)
        return self

    def set_language(self, language):
        if language in self._supported_languages:
            self._language = language
        else:
            raise AttributeError(
                'This language "%s" is not supported' % language)
        return self

    def set_data(self, data):
        self._data = data
        return self

    def update_data(self, values):
        if self._data is None:
            self._data = {}
        self._data.update(values)
        return self

    def set_pagination(self, **kwargs):
        return self.update_data(HttpTransportPagination(**kwargs).to_value())

    def set_ordering(self, **kwargs):
        return self.update_data(HttpTransportOrdering(**kwargs).to_value())

    def set_method(self, method):
        if method in self._supported_methods:
            self._method = method
        else:
            raise AttributeError(
                'This http method "%s" is not supported' % method)
        return self

    def _prepare_pagination(self, **kwargs):
        pass

    def _handle_response(self, response):
        return response

    def __getattr__(self, name):
        return self.set_method(name)

    def api_request(self, url, **kwargs):
        return api_request(url, **kwargs)

    def request(self, **kwargs):
        if 'language' in kwargs:
            self.set_language(kwargs['language'])
        if 'url' in kwargs:
            url = kwargs.pop('url')
            self.set_url(url, **kwargs)
        if not self._url:
            raise AttributeError(
                'Absent url parameter. Use set_url method or pass '
                'url parameter in this method.')
        response = self.api_request(
            self._url, method=self._method,
            headers=self._headers, data=self._data)
        if 'handler' in kwargs:
            return kwargs['handler'](response)
        else:
            return self._handle_response(response)

    def __call__(self, **kwargs):
        return self.request(**kwargs)
