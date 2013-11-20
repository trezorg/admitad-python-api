from pyadmitad.items.base import Item


__all__ = (
    'Banners',
    'BannersForWebsite',
)


class Banners(Item):
    """
    List of banners

    Required scope - "banners"
    """

    URL = Item.prepare_url('banners/%(id)s')

    def get(self, _id, **kwargs):
        """
        Here _id is an id of advertising campaign

        res = client.Banners.get(_id=2)
        res = client.Banners.get(2)
        res = client.Banners.get(2, limit=2)

        """
        kwargs['url'] = self.URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)


class BannersForWebsite(Item):
    """
    List of banners for the website

    Required scope - "banners_for_website"
    """

    URL = Item.prepare_url('banners/%(id)s/website/%(w_id)s')

    def get(self, _id, w_id, **kwargs):
        """
        Here _id is an id of advertising campaign and
        w_id is a id of website

        res = client.BannersForWebsite.get(_id=2, w_id=3)
        res = client.BannersForWebsite.get(2, 3)
        res = client.BannersForWebsite.get(2, 3, limit=5)
        """
        kwargs['url'] = self.URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['w_id'] = self.sanitize_id(w_id)
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)
