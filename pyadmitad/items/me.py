from pyadmitad.items.base import Item


class Me(Item):
    """
    Get private information

    Required scope - "private_data"
    """

    def __call__(self, **kwargs):
        return self.get(**kwargs)

    URL = Item.prepare_url('me')

    def get(self, **kwargs):
        """
        res = client.Me.get()
        res = client.Me.get(language='ru')
        """
        kwargs['url'] = self.URL
        return self.transport.GET.request(**kwargs)
