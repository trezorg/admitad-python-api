from pyadmitad.items.base import Item
from pyadmitad.constants import *


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
