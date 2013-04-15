# default values
DEFAULT_REQUEST_TIMEOUT = 60
DEFAULT_LANGUAGE = 'ru'
MAX_PAGINATION_LIMIT = 200

# urls
BASE_URL = 'https://api.admitad.com/%(language)s/'
# authorizing urls
AUTHORIZE_URL = '%s%s' % (BASE_URL,  'authorize/')
TOKEN_URL = '%s%s' % (BASE_URL,  'token/')
# private info urls(user data)
ME_URL = '%s%s' % (BASE_URL,  'me/')
# public data urls
WEBSITE_TYPES_URL = '%s%s' % (BASE_URL,  'websites/kinds/')
WEBSITE_REGIONS_URL = '%s%s' % (BASE_URL,  'websites/regions/')
LANGUAGES_URL = '%s%s' % (BASE_URL,  'languages/')
LANGUAGES_SINGLE_URL = '%s%s' % (BASE_URL,  'languages/%(code)s/')
CURRENCIES_URL = '%s%s' % (BASE_URL,  'currencies/')
ADVERTISER_SERVICES_URL = '%s%s' % (BASE_URL,  'adservices/')
ADVERTISER_SERVICES_SINGLE_URL = '%s%s' % (BASE_URL,  'adservices/%(id)s/')
ADVERTISER_SERVICES_KIND_URL = '%s%s' % (BASE_URL,  'adservices/kind/%(kind)s/')
ADVERTISER_SERVICES_KIND_SINGLE_URL = '%s%s' % (
    BASE_URL,  'adservices/%(id)s/kind/%(kind)s/')
ADVCAMPAIGNS_CATEGORIES_URL = '%s%s' % (BASE_URL,  'categories/')
ADVCAMPAIGNS_CATEGORIES_SINGLE_URL = '%s%s' % (BASE_URL,  'categories/%(id)s/')
# coupons
COUPONS_URL = '%s%s' % (BASE_URL,  'coupons/')
COUPONS_WEBSITE_URL = '%s%s' % (BASE_URL,  'coupons/website/%(id)s/')
COUPONS_SINGLE_URL = '%s%s' % (BASE_URL,  'coupons/%(id)s/')
COUPONS_WEBSITE_SINGLE_URL = '%s%s' % (
    BASE_URL,  'coupons/%(c_id)s/website/%(id)s/')
# websites
WEBSITES_URL = '%s%s' % (BASE_URL,  'websites/')
WEBSITES_SINGLE_URL = '%s%s' % (BASE_URL,  'websites/%(id)s/')

