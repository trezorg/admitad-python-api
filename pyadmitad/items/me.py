from pyadmitad.items.base import Item
from pyadmitad.constants import *


class Me(Item):

    def __call__(self, **kwargs):
        return self.get(**kwargs)

    def get(self, **kwargs):
        kwargs['url'] = ME_URL
        return self.transport.GET(**kwargs)
