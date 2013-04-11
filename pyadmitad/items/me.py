from pyadmitad.items.base import Item
from pyadmitad.constants import *


class Me(Item):

    def __call__(self, **kwargs):
        return self.get(**kwargs)

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
        print client.Me.get()
        print client.Me.get(language='ru')
        """
        kwargs['url'] = ME_URL
        return self.transport.GET(**kwargs)
