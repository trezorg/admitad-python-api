from pyadmitad.items.base import Item


__all__ = (
    'Websites',
)


class Websites(Item):
    """
    List of websites

    How to prepare client:

    scope = "websites"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """
    URL = Item.prepare_url('websites')
    SINGLE_URL = Item.prepare_url('websites/%(id)s')

    STATUS_FILTERING = ('new', 'pending', 'active', 'suspended', 'declined')
    CAMPAIGN_STATUS_FILTERING = ('pending', 'active', 'declined', 'disabled')
    FILTERING = {
        'status': lambda x: x if x in Websites.STATUS_FILTERING else None,
        'campaign_status': (
            lambda x: x if x in Websites.CAMPAIGN_STATUS_FILTERING else None),
    }

    def get(self, **kwargs):
        """
        res = client.Websites.get()
        res = client.Websites.get(status='new', campaign_status='active')

        """
        kwargs['url'] = self.URL
        kwargs['allowed_filtering'] = self.FILTERING
        return self.transport.GET.set_pagination(**kwargs).\
            set_filtering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        res = client.Websites.getOne(_id=2)
        res = client.Websites.getOne2(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.GET.request(**kwargs)
