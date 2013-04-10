# default values
DEFAULT_REQUEST_TIMEOUT = 60
DEFAULT_LANGUAGE = 'ru'
MAX_PAGINATION_LIMIT = 200

# urls
BASE_URL = 'https://api.admitad.com/%(language)s/'
AUTHORIZE_URL = '%s%s' % (BASE_URL,  'authorize/')
TOKEN_URL = '%s%s' % (BASE_URL,  'token/')
ME_URL = '%s%s' % (BASE_URL,  'me/')
WEBSITE_TYPES_URL = '%s%s' % (BASE_URL,  'websites/kinds/')

