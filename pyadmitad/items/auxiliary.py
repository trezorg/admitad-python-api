from pyadmitad.items.base import Item
from pyadmitad.constants import *


__all__ = ('WebsiteTypes', 'WebsiteRegions', 'SystemLanguages')


class WebsiteTypes(Item):

    def get(self, **kwargs):
        """
        scope = "public_data"
        client = api.get_oauth_password_client(
            client_id,
            client_secret,
            username,
            password,
            scope
        )
        print client.WebsiteTypes.get()
        print client.WebsiteTypes.get(limit=2, offset=1)
        print client.WebsiteTypes.get(limit=2, offset=1, language='ru')
        """
        kwargs['url'] = WEBSITE_TYPES_URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)


class WebsiteRegions(Item):

    def get(self, **kwargs):
        """
        scope = "public_data"
        client = api.get_oauth_password_client(
            client_id,
            client_secret,
            username,
            password,
            scope
        )
        print client.WebsiteRegions.get()
        print client.WebsiteRegions.get(limit=2, offset=1)
        print client.WebsiteRegions.get(limit=2, offset=1, language='ru')
        """
        kwargs['url'] = WEBSITE_REGIONS_URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)


class SystemLanguages(Item):

    def get(self, **kwargs):
        """
        scope = "public_data"
        client = api.get_oauth_password_client(
            client_id,
            client_secret,
            username,
            password,
            scope
        )
        print client.SystemLanguages.get()
        print client.SystemLanguages.get(limit=2, offset=1)
        """
        kwargs['url'] = LANGUAGES_URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)

    def getOne(self, code='ru'):
        """
        scope = "public_data"
        client = api.get_oauth_password_client(
            client_id,
            client_secret,
            username,
            password,
            scope
        )
        print client.SystemLanguages.getOne(code='ru')
        """
        return self.transport.GET.request(url=LANGUAGES_SINGLE_URL, code=code)
