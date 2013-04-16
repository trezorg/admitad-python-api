# API date-format
DATE_FORMAT = "%d.%m.%Y"

# default values
DEFAULT_REQUEST_TIMEOUT = 60
DEFAULT_LANGUAGE = 'ru'
MAX_PAGINATION_LIMIT = 200
SUB_ID_MAX_LENGTH = 50


def prepare_url(path):
    url = '%s%s' % (BASE_URL,  path)
    if not url.endswith('/'):
        url += '/'
    return url

# urls
BASE_URL = 'https://api.admitad.com/'
BASE_URL = 'https://api.admitad.trezor.by/'

# authorizing urls
AUTHORIZE_URL = prepare_url('authorize')
TOKEN_URL = prepare_url('token')

# private info urls(user data)
ME_URL = prepare_url('me')

# public data urls
WEBSITE_TYPES_URL = prepare_url('websites/kinds')
WEBSITE_REGIONS_URL = prepare_url('websites/regions')
LANGUAGES_URL = prepare_url('languages')
LANGUAGES_SINGLE_URL = prepare_url('languages/%(code)s')
CURRENCIES_URL = prepare_url('currencies')
ADVERTISER_SERVICES_URL = prepare_url('adservices')
ADVERTISER_SERVICES_SINGLE_URL = prepare_url('adservices/%(id)s')
ADVERTISER_SERVICES_KIND_URL = prepare_url('adservices/kind/%(kind)s')
ADVERTISER_SERVICES_KIND_SINGLE_URL = prepare_url(
    'adservices/%(id)s/kind/%(kind)s')
CAMPAIGN_CATEGORIES_URL = prepare_url('categories')
CAMPAIGN_CATEGORIES_SINGLE_URL = prepare_url('categories/%(id)s')

# coupons
COUPONS_URL = prepare_url('coupons')
COUPONS_WEBSITE_URL = prepare_url('coupons/website/%(id)s')
COUPONS_SINGLE_URL = prepare_url('coupons/%(id)s')
COUPONS_WEBSITE_SINGLE_URL = prepare_url('coupons/%(c_id)s/website/%(id)s')

# websites
WEBSITES_URL = prepare_url('websites')
WEBSITES_SINGLE_URL = prepare_url('websites/%(id)s')

#statistics
STATISTIC_WEBSITES_URL = prepare_url('statistics/websites')
STATISTIC_CAMPAIGNS_URL = prepare_url('statistics/campaigns')
STATISTIC_DAYS_URL = prepare_url('statistics/dates')
