from pyadmitad.items.base import Item
from pyadmitad.constants import *


__all__ = (
    'WebsiteTypes',
    'WebsiteRegions',
    'SystemLanguages',
    'SystemCurrencies',
    'AdvertiserServices',
    'AdvcampaignsCategories',
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


class AdvertiserServices(Item):
    """
    List of advertiser services

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
        print client.AdvertiserServices.get()
        print client.AdvertiserServices.get(limit=2, offset=1)
        """
        kwargs['url'] = ADVERTISER_SERVICES_URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        print client.AdvertiserServices.getOne(_id=2)
        print client.AdvertiserServices.getOne(1)
        """
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['url'] = ADVERTISER_SERVICES_SINGLE_URL
        return self.transport.GET.request(**kwargs)

    def getForKind(self, kind=None, **kwargs):
        """
        Returns advertiser services for website types

        print client.AdvertiserServices.getForKind(kind='website')
        print client.AdvertiserServices.getForKind('website')
        """
        kwargs['kind'] = self.sanitize_non_blank_value(kind, 'kind')
        kwargs['url'] = ADVERTISER_SERVICES_KIND_URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)

    def getForKindOne(self, _id, kind, **kwargs):
        """
        Returns advertiser service for website types

        print client.AdvertiserServices.getForKindOne(_id=2, kind='website')
        print client.AdvertiserServices.getForKindOne(2, 'website')
        """
        kwargs['kind'] = self.sanitize_non_blank_value(kind, 'kind')
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['url'] = ADVERTISER_SERVICES_KIND_SINGLE_URL
        return self.transport.GET.request(**kwargs)


class AdvcampaignsCategories(Item):
    """
    List of advcampaigns categories

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
        print client.AdvcampaignsCategories.get()
        print client.AdvcampaignsCategories.get(limit=2, offset=1)
        """
        kwargs['url'] = ADVCAMPAIGNS_CATEGORIES_URL
        kwargs['allowed_ordering'] = ('name',)
        return self.transport.GET.set_pagination(**kwargs).\
            set_ordering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        print client.AdvcampaignsCategories.getOne(_id=2)
        print client.AdvcampaignsCategories.getOne(2)
        """
        kwargs['url'] = ADVCAMPAIGNS_CATEGORIES_SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.GET.request(**kwargs)
