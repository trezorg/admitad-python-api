from pyadmitad.items.base import Item


__all__ = (
    'Campaigns',
    'CampaignsForWebsite',
    'CampaignsManage',
)


class Campaigns(Item):
    """
    List of advertising campaigns

    Required scope - "advcampaigns"
    """
    URL = Item.prepare_url('advcampaigns')
    SINGLE_URL = Item.prepare_url('advcampaigns/%(id)s')

    def get(self, **kwargs):
        """
        res = client.Campaigns.get()
        res = client.Campaigns.get(limit=2)

        """
        kwargs['url'] = self.URL
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        Here _id is an a campaign id

        res = client.Campaigns.getOne(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('GET').request(**kwargs)


class CampaignsForWebsite(Item):
    """
    List of advertising campaigns for a website

    Required scope - "advcampaigns_for_website"
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
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)

    def getOne(self, _id, c_id, **kwargs):
        """
        Here _id is a website id and c_id is a campaign id

        res = client.CampaignsForWebsite.getOne(6, 22)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['c_id'] = self.sanitize_id(c_id)
        return self.transport.set_method('GET').request(**kwargs)


class CampaignsManage(Item):
    """
    Manage an advertising campaign

    Required scope - "manage_advcampaigns"
    """
    CONNECT_URL = Item.prepare_url('advcampaigns/%(c_id)s/attach/%(w_id)s')
    DISCONNECT_URL = Item.prepare_url('advcampaigns/%(c_id)s/detach/%(w_id)s')

    def _request(self, c_id, w_id, **kwargs):
        kwargs['c_id'] = self.sanitize_id(c_id)
        kwargs['w_id'] = self.sanitize_id(w_id)
        return self.transport.set_method('POST').request(**kwargs)

    def connect(self, c_id, w_id, **kwargs):
        """
        Connect an advertising campaign for a website
        Here w_id is a website id and c_id is a campaign id

        res = client.CampaignsManage.connect(6, 22)
        res = client.CampaignsManage.connect(c_id=6, w_id=22)

        """
        kwargs['url'] = self.CONNECT_URL
        return self._request(c_id, w_id, **kwargs)

    def disconnect(self, c_id, w_id, **kwargs):
        """
        Disconnect an advertising campaign from a website
        Here w_id is a website id and c_id is a campaign id

        res = client.CampaignsManage.disconnect(6, 22)
        res = client.CampaignsManage.disconnect(c_id=6, w_id=22)

        """
        kwargs['url'] = self.DISCONNECT_URL
        return self._request(c_id, w_id, **kwargs)
