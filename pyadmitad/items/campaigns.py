from pyadmitad.items.base import Item


__all__ = (
    'Campaigns',
    'CampaignsForWebsite',
)


class Campaigns(Item):
    """
    List of advertising campaigns

    How to prepare client:

    scope = "advcampaigns"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """
    URL = Item.prepare_url('advcampaigns')
    SINGLE_URL = Item.prepare_url('advcampaigns/%(id)s')

    def get(self, **kwargs):
        """
        res = client.Campaigns.get()
        res = client.Campaigns.get(limit=2)

        """
        kwargs['url'] = self.URL
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        Here _id is an a campaign id

        res = client.Campaigns.getOne(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.GET.request(**kwargs)


class CampaignsForWebsite(Item):
    """
    List of advertising campaigns for a website

    How to prepare client:

    scope = "advcampaigns_for_website"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """
    URL = Item.prepare_url('advcampaigns/website/%(id)s')
    SINGLE_URL = Item.prepare_url('advcampaigns/%(c_id)s/website/%(id)s')

    def get(self, _id, **kwargs):
        """
        Here _id is a website id

        res = client.CampaignsForWebsite.get(22)
        res = client.CampaignsForWebsite.get(limit=2)

        """
        kwargs['url'] = self.URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.GET.set_pagination(**kwargs).request(**kwargs)

    def getOne(self, _id, c_id, **kwargs):
        """
        Here _id is a website id and c_id is a campaign id

        res = client.CampaignsForWebsite.getOne(6, 22)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['c_id'] = self.sanitize_id(c_id)
        return self.transport.GET.request(**kwargs)
