import requests
from base64 import b64encode
import json
import urllib
try:
    import urlparse
except ImportError:
    import urllib.parse
import uuid
import logging
from pyadmitad.constants import *
from pyadmitad.exceptions import *


LOG = logging.getLogger(__file__)
LOG.addHandler(logging.StreamHandler())


def to_json(content):
    try:
        return json.loads(content)
    except (TypeError, ValueError):
        return content


def debug_log(value, debug=True):
    if debug:
        LOG.setLevel(logging.DEBUG)
        LOG.debug(value)
    else:
        LOG.setLevel(logging.NOTSET)


def prepare_request_data(
        data=None, headers=None, method='GET',
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


def api_request(
        url, data=None, headers=None, method='GET',
        timeout=None, ssl_verify=False, debug=False):
    kwargs = prepare_request_data(
        data=data, headers=headers, method=method,
        timeout=timeout, ssl_verify=ssl_verify)
    status_code = 500
    content = u''
    try:
        response = requests.request(method, url, **kwargs)
        debug_log(u'Request url: %s' % response.url, debug)
        if method == 'POST':
            debug_log(u'Request body: %s' % response.request.body, debug)
        status_code = response.status_code
        content = response.content
        if status_code >= 400:
            response.raise_for_status()
        return response.json()
    except requests.HTTPError as err:
        raise HttpException(status_code, to_json(content), err)
    except requests.RequestException as err:
        raise ConnectionException(err)
    except (ValueError, TypeError) as err:
        raise JsonException(err)


def get_credentials(client_id, client_secret):
    return b64encode(
        ("%s:%s" % (client_id, client_secret)).encode('utf-8')
    ).decode('utf-8')


def api_post_request(url, **kwargs):
    kwargs['method'] = "POST"
    return api_request(url, **kwargs)


def api_get_request(url, **kwargs):
    kwargs['method'] = "GET"
    return api_request(url, **kwargs)


def build_authorization_headers(access_token):
    return {'Authorization': "Bearer %s" % access_token}


def build_headers(access_token, user_agent=None, language=None):
    headers = build_authorization_headers(access_token)
    headers['Connection'] = 'Keep-Alive'
    if user_agent:
        headers['User-Agent'] = user_agent
    if language:
        headers['Content-Language'] = language
    return headers


def oauth_password_authorization(data):
    """
    OAuth2 password authorization
    Used to get an access_token with the user's password and username
    The function parameter should be a dictionary with next structure:
    data = {
        'client_id': '',
        'client_secret': '',
        'username': '',
        'password': '',
        'scope': ''
    }
    """
    client_id = data['client_id']
    client_secret = data['client_secret']
    params = {
        'grant_type': 'password',
        'client_id': client_id,
        'username': data['username'],
        'password': data['password'],
        'scope': data['scopes']
    }
    credentials = get_credentials(client_id, client_secret)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic %s' % credentials
    }
    return api_post_request(TOKEN_URL, data=params, headers=headers)


def oauth_refresh_access_token(data):
    """
    refresh an access token. Returns dictionary with new access_token.
    data['access-token']
    The function parameter should be a dictionary with next structure:
    data = {
        'refresh_token': '',
        'client_secret': '',
        'client_id': ''
    }
    """
    refresh_token = data['refresh_token']
    client_id = data['client_id']
    client_secret = data['client_secret']
    params = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return api_post_request(TOKEN_URL, data=params, headers=headers)


def oauth_client_authorization(data):
    """
    OAuth2 client authorization.
    Used to get an access_token with the oauth client credentials
    The function parameter should be a dictionary with next structure:
    data = {
        'client_secret': '',
        'client_id': ''
        'scopes': '',
    }
    """
    client_id = data['client_id']
    client_secret = data['client_secret']
    params = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'scope': data['scopes']
    }
    credentials = get_credentials(client_id, client_secret)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic %s' % credentials
    }
    return api_post_request(TOKEN_URL, data=params, headers=headers)


class OAuthServerAuthorisation(object):
    """
    OAuth2 server authorization.
    Used to get an access_token with the web authentication
    """

    def __init__(self, data):
        """
        The constructor parameter should be a dictionary with next structure:
        data = {
            'client_secret': '',
            'client_id': ''
            'scopes': '',
            'redirect_uri': '',
        }
        """
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
        return "%s?%s" % (AUTHORIZE_URL, urllib.urlencode(params))

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
        response = api_post_request(TOKEN_URL, data=params, headers=headers)
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


class HttpTransportFiltering(object):

    def __init__(self, **kwargs):
        self.result = {}
        allowed_filtering = kwargs.get('allowed_filtering', {}) or {}
        if not allowed_filtering:
            return
        self.allowed_filtering = allowed_filtering
        self.check_filtering(**kwargs)

    def check_value(self, val, func):
        """
        Should return False in boolean meaning
        in case of unsupported or wrong value
        """
        if not func:
            return val
        try:
            return func(val)
        except (TypeError, ValueError):
            pass

    def check_values(self, values, func):
        return filter(None, [self.check_value(value, func) for value in values])

    def check_filtering(self, **filtering):
        for val in self.allowed_filtering:
            value = filtering.get(val)
            if value is None:
                continue
            if not isinstance(value, (tuple, list)):
                value = [value]
            func = self.allowed_filtering[val]
            res = self.check_values(value, func)
            if res:
                self.result.setdefault(val, []).extend(res)

    def to_value(self):
        for key in self.result:
            self.result[key] = list(set(self.result[key]))
        return self.result


class HttpTransport(object):

    SUPPORTED_METHODS = ('GET', 'POST')
    SUPPORTED_LANGUAGES = ('ru', 'en', 'de', 'pl')

    def __init__(self, access_token, method=None, user_agent=None, debug=False):
        self._headers = build_headers(access_token, user_agent=user_agent)
        self._method = method or 'GET'
        self._data = None
        self._url = None
        self._language = None
        self._debug = debug

    def set_url(self, url, **kwargs):
        self._url = url % kwargs
        return self

    def set_language(self, language):
        if language in self.SUPPORTED_LANGUAGES:
            self._language = language
            self._headers['Content-Language'] = language
        else:
            raise AttributeError(
                'This language "%s" is not supported' % language)
        return self

    def set_data(self, data):
        self._data = data
        return self

    def clean_data(self):
        self._data = None
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

    def set_filtering(self, **kwargs):
        return self.update_data(HttpTransportFiltering(**kwargs).to_value())

    def set_method(self, method):
        if method in self.SUPPORTED_METHODS:
            self._method = method
        else:
            raise AttributeError(
                'This http method "%s" is not supported' % method)
        # here we should clean data
        return self.clean_data()

    def set_debug(self, debug):
        self._debug = debug
        return self

    @staticmethod
    def _handle_response(response):
        return response

    @staticmethod
    def api_request(url, **kwargs):
        return api_request(url, **kwargs)

    def request(self, **kwargs):
        if 'language' in kwargs:
            self.set_language(kwargs['language'])
        if 'url' in kwargs:
            self.set_url(kwargs.pop('url'), **kwargs)
        if 'debug' in kwargs:
            self.set_debug(kwargs.pop('debug'))
        if not self._url:
            raise AttributeError(
                'Absent url parameter. Use set_url method or pass '
                'url parameter in this method.')
        requests_kwargs = {
            'method': self._method,
            'headers': self._headers,
            'data': self._data,
            'debug': self._debug
        }
        response = self.api_request(self._url, **requests_kwargs)
        return kwargs.get('handler', self._handle_response)(response)

    def __call__(self, **kwargs):
        return self.request(**kwargs)
