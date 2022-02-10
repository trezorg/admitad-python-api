# coding: utf-8
from __future__ import unicode_literals

from admitad.items.base import Item


__all__ = [
    'ShortLinks'
]


class ShortLinks(Item):

    SCOPE = 'short_links'

    URL = Item.prepare_url('short_links')
    SINGLE_URL = Item.prepare_url('shortlink/modify/')

    def get(self, **kwargs):
        """
        Args:
            link (str)

        """
        filtering = {
            'filter_by': kwargs,
            'available': {
                'link': lambda x: Item.sanitize_string_value(x, 'link', blank=True),
            }
        }

        return self.transport.get() \
                   .set_pagination(**kwargs) \
                   .set_filtering(filtering) \
                   .request(url=self.URL)
