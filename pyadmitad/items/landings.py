from pyadmitad.items.base import Item

__all__ = [
    'Landings',
    'LandingsForWebsite',
]


class Landings(Item):

    URL = Item.prepare_url('landings/%(campaign_id)s')

    def get(self, campaign_id, **kwargs):
        kwargs['url'] = self.URL
        kwargs['campaign_id'] = self.sanitize_id(campaign_id)
        return self.transport.get().set_pagination(**kwargs).request(**kwargs)


class LandingsForWebsite(Item):

    URL = Item.prepare_url('landings/%(campaign_id)s/website/%(website_id)s')

    def get(self, campaign_id, website_id, **kwargs):
        kwargs['url'] = self.URL
        kwargs['campaign_id'] = self.sanitize_id(campaign_id)
        kwargs['website_id'] = self.sanitize_id(website_id)
        return self.transport.get().set_pagination(**kwargs).request(**kwargs)
