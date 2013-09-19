CURRENCIES = ('USD', 'RUB', 'EUR')
# API date-format
DATE_FORMAT = "%d.%m.%Y"
LONG_DATE_FORMAT = "%d.%m.%Y %H:%M:%S"

# default values
DEFAULT_REQUEST_TIMEOUT = 60
DEFAULT_LANGUAGE = 'ru'
MAX_PAGINATION_LIMIT = 200
SUB_ID_MAX_LENGTH = 50

# urls
BASE_URL = 'https://api.admitad.com/'
AUTHORIZE_URL = '%s%s' % (BASE_URL, 'authorize/')
TOKEN_URL = '%s%s' % (BASE_URL, 'token/')
