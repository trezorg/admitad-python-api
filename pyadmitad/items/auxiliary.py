from pyadmitad.items.base import Item


__all__ = (
    'WebsiteTypes',
    'WebsiteRegions',
    'SystemLanguages',
    'SystemCurrencies',
    'AdvertiserServices',
    'CampaignCategories',
)


class WebsiteTypes(Item):
    """
    List of websites types

    Required scope - "public_data"
    """

    URL = Item.prepare_url('websites/kinds')

    def get(self, **kwargs):
        """
        res = client.WebsiteTypes.get()
        res = client.WebsiteTypes.get(limit=2, offset=1)
        res = client.WebsiteTypes.get(limit=2, offset=1, language='ru')
        """
        kwargs['url'] = self.URL
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)


class WebsiteRegions(Item):
    """
    List of websites regions

    Required scope - "public_data"
    """

    URL = Item.prepare_url('websites/regions')

    def get(self, **kwargs):
        """
        res = client.WebsiteRegions.get()
        res = client.WebsiteRegions.get(limit=2, offset=1)
        res = client.WebsiteRegions.get(limit=2, offset=1, language='ru')
        """
        kwargs['url'] = self.URL
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)


class SystemLanguages(Item):
    """
    List of system languages

    Required scope - "public_data"
    """

    URL = Item.prepare_url('languages')
    SINGLE_URL = Item.prepare_url('languages/%(code)s')

    def get(self, **kwargs):
        """
        res = client.SystemLanguages.get()
        res = client.SystemLanguages.get(limit=2, offset=1)
        """
        kwargs['url'] = self.URL
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)

    def getOne(self, code='ru'):
        """
        res = client.SystemLanguages.getOne(code='ru')
        """
        return self.transport.set_method('GET').request(url=self.SINGLE_URL, code=code)


class SystemCurrencies(Item):
    """
    List of system currencies

    Required scope - "public_data"
    """

    URL = Item.prepare_url('currencies')

    def get(self, **kwargs):
        """
        res = client.SystemCurrencies.get()
        res = client.SystemCurrencies.get(limit=2, offset=1)
        """
        kwargs['url'] = self.URL
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)


class AdvertiserServices(Item):
    """
    List of advertiser services

    Required scope - "public_data"
    """

    URL = Item.prepare_url('adservices')
    SINGLE_URL = Item.prepare_url('adservices/%(id)s')
    KIND_URL = Item.prepare_url('adservices/kind/%(kind)s')
    KIND_SINGLE_URL = Item.prepare_url('adservices/%(id)s/kind/%(kind)s')

    def get(self, **kwargs):
        """
        res = client.AdvertiserServices.get()
        res = client.AdvertiserServices.get(limit=2, offset=1)
        """
        kwargs['url'] = self.URL
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        res = client.AdvertiserServices.getOne(_id=2)
        res = client.AdvertiserServices.getOne(1)
        """
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['url'] = self.SINGLE_URL
        return self.transport.set_method('GET').request(**kwargs)

    def getForKind(self, kind=None, **kwargs):
        """
        Returns advertiser services for website types

        res = client.AdvertiserServices.getForKind(kind='website')
        res = client.AdvertiserServices.getForKind('website')
        """
        kwargs['kind'] = self.sanitize_non_blank_value(kind, 'kind')
        kwargs['url'] = self.KIND_URL
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)

    def getForKindOne(self, _id, kind, **kwargs):
        """
        Returns advertiser service for website types

        res = client.AdvertiserServices.getForKindOne(_id=2, kind='website')
        res = client.AdvertiserServices.getForKindOne(2, 'website')
        """
        kwargs['kind'] = self.sanitize_non_blank_value(kind, 'kind')
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['url'] = self.KIND_SINGLE_URL
        return self.transport.set_method('GET').request(**kwargs)


class CampaignCategories(Item):
    """
    List of campaigns categories

    Required scope - "public_data"
    """

    ORDERING = ('name',)

    URL = Item.prepare_url('categories')
    SINGLE_URL = Item.prepare_url('categories/%(id)s')

    def get(self, **kwargs):
        """
        res = client.CampaignCategories.get()
        res = client.CampaignCategories.get(limit=2, offset=1)
        """
        kwargs['url'] = self.URL
        kwargs['allowed_ordering'] = self.ORDERING
        return self.transport.set_method('GET').set_pagination(**kwargs).\
            set_ordering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        res = client.CampaignCategories.getOne(_id=2)
        res = client.CampaignCategories.getOne(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('GET').request(**kwargs)
