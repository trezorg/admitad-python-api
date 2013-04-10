# default values
DEFAULT_REQUEST_TIMEOUT = 60
DEFAULT_LANGUAGE = 'ru'

# urls
BASE_URL = 'https://api.admitad.com/%(language)s/'
AUTHORIZE_URL = '%s%s' % (BASE_URL,  'authorize/')
TOKEN_URL = '%s%s' % (BASE_URL,  'token/')
ME_URL = '%s%s' % (BASE_URL,  'me/')

