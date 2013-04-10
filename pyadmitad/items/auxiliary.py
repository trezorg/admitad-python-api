from pyadmitad.items.base import Item
from pyadmitad.constants import *


class WebsiteTypes(Item):

    def getAll(self, **kwargs):
        kwargs['url'] = WEBSITE_TYPES_URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)
