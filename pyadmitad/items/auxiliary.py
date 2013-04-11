from pyadmitad.items.base import Item
from pyadmitad.constants import *


__all__ = (
    'WebsiteTypes',
    'WebsiteRegions',
    'SystemLanguages',
    'SystemCurrencies'
)


class WebsiteTypes(Item):
    """
    List of websites types

    How to prepare client:

    scope = "public_data"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """
    def get(self, **kwargs):
        """
        print client.WebsiteTypes.get()
        print client.WebsiteTypes.get(limit=2, offset=1)
        print client.WebsiteTypes.get(limit=2, offset=1, language='ru')
        """
        kwargs['url'] = WEBSITE_TYPES_URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)


class WebsiteRegions(Item):
    """
    List of websites regions

    How to prepare client:

    scope = "public_data"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """
    def get(self, **kwargs):
        """
        print client.WebsiteRegions.get()
        print client.WebsiteRegions.get(limit=2, offset=1)
        print client.WebsiteRegions.get(limit=2, offset=1, language='ru')
        """
        kwargs['url'] = WEBSITE_REGIONS_URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)


class SystemLanguages(Item):
    """
    List of system languages

    How to prepare client:

    scope = "public_data"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """

    def get(self, **kwargs):
        """
        print client.SystemLanguages.get()
        print client.SystemLanguages.get(limit=2, offset=1)
        """
        kwargs['url'] = LANGUAGES_URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)

    def getOne(self, code='ru'):
        """
        print client.SystemLanguages.getOne(code='ru')
        """
        return self.transport.GET.request(url=LANGUAGES_SINGLE_URL, code=code)


class SystemCurrencies(Item):
    """
    List of system currencies

    How to prepare client:

    scope = "public_data"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """
    def get(self, **kwargs):
        """
        print client.SystemCurrencies.get()
        print client.SystemCurrencies.get(limit=2, offset=1)
        """
        kwargs['url'] = CURRENCIES_URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)
