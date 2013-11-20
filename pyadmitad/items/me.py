from pyadmitad.items.base import Item


__all__ = (
    'Me',
    'Balance',
)


class Me(Item):
    """
    Get private information

    Required scope - "private_data"|"private_data_email"|"private_data_phone"
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
        return self.transport.set_method("GET").request(**kwargs)


class Balance(Item):
    """
    Get balance information

    Required scope - "private_data_balance"
    """

    def __call__(self, **kwargs):
        return self.get(**kwargs)

    URL = Item.prepare_url('me/balance')

    def get(self, **kwargs):
        """
        res = client.Balance.get()
        """
        kwargs['url'] = self.URL
        return self.transport.set_method('GET').set_method("GET").request(**kwargs)
