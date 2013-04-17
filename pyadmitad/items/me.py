from pyadmitad.items.base import Item


class Me(Item):

    def __call__(self, **kwargs):
        return self.get(**kwargs)

    URL = Item.prepare_url('me')

    def get(self, **kwargs):
        """
        scope = "private_data"
        client = api.get_oauth_password_client(
            client_id,
            client_secret,
            username,
            password,
            scope
        )
        res = client.Me.get()
        res = client.Me.get(language='ru')
        """
        kwargs['url'] = self.URL
        return self.transport.GET.request(**kwargs)
