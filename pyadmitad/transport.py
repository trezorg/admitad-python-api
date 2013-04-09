import requests
from base64 import b64encode
import simplejson
import urllib
import urlparse
import uuid
from .constants import *
from .exceptions import *


def api_request(url, data=None, headers=None, method='GET', timeout=None):
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
    status_code = 500
    try:
        response = requests.request(method, url, **kwargs)
        status_code = response.status_code
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as err:
        raise HttpException(status_code, err)
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


def prepare_api_url(url, language=DEFAULT_LANGUAGE):
    return url % {'language': language}


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
        prepare_api_url(TOKEN_URL, language), data=params, headers=headers)


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
        prepare_api_url(TOKEN_URL, language), data=params, headers=headers)


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
            prepare_api_url(AUTHORIZE_URL, self.language),
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
            prepare_api_url(TOKEN_URL, self.language),
            data=params, headers=headers)
        if 'access_token' not in response:
            raise ApiException('Invalid response. The access_token is absent.')
        return response
