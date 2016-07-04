from pyadmitad.items.base import Item


__all__ = [
    'News',
]


class News(Item):

    URL = Item.prepare_url('news')
    SINGLE_URL = Item.prepare_url('news/%(news_id)s')

    def get(self, **kwargs):
        kwargs['url'] = self.URL
        return self.transport.get().set_pagination(**kwargs).request(**kwargs)

    def getOne(self, news_id, **kwargs):
        kwargs['url'] = self.SINGLE_URL
        kwargs['news_id'] = self.sanitize_id(news_id)
        return self.transport.get().set_pagination(**kwargs).request(**kwargs)
