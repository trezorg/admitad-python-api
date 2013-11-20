from pyadmitad.items.base import Item


__all__ = (
    'Coupons',
    'CouponsForWebsite',
)


class CouponsBase(Item):

    ORDERING = ('name', 'date_start', 'date_end', 'rating',)
    FILTERING = {
        'campaign': int,
        'campaign_category': int,
        'category': int,
        'type': int
    }


class Coupons(CouponsBase):
    """
    List of coupons

    Required scope - "coupons"
    """

    URL = Item.prepare_url('coupons')
    SINGLE_URL = Item.prepare_url('coupons/%(id)s')

    def get(self, **kwargs):
        """
        res = client.Coupons.get()
        res = client.Coupons.get(order_by=date_start)
        res = client.Coupons.get(order_by=-date_end)
        res = client.Coupons.get(campaign=1, category=2)

        If you want to filter by many values of the same key:
            on example - campaign=1, campaign=2:

            use campaign=[1, 2]

        res = client.Coupons.get(campaign=[1, 2], category=2)

        """
        kwargs['url'] = self.URL
        kwargs['allowed_ordering'] = self.ORDERING
        kwargs['allowed_filtering'] = self.FILTERING
        return self.transport.set_method('GET').set_pagination(**kwargs).\
            set_ordering(**kwargs).set_filtering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        res = client.Coupons.getOne(_id=2)
        res = client.Coupons.getOne(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('GET').request(**kwargs)


class CouponsForWebsite(CouponsBase):
    """
    List of the website coupons

    Required scope - "coupons_for_website"
    """

    URL = Item.prepare_url('coupons/website/%(id)s')
    SINGLE_URL = Item.prepare_url('coupons/%(c_id)s/website/%(id)s')

    def get(self, _id, **kwargs):
        """
        Here id is a websites id

        res = client.CouponsForWebsite.get(_id=2)
        res = client.CouponsForWebsite.get(2)
        res = client.CouponsForWebsite.get(2, order_by=date_start)
        res = client.CouponsForWebsite.get(2, campaign=1, category=2)

        If you want to filter by many values of the same key:
            on example - campaign=1, campaign=2:

            use campaign=[1, 2]

        res = client.CouponsForWebsite.get(2, campaign=[1, 2], category=2)

        """
        kwargs['url'] = self.URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['allowed_ordering'] = self.ORDERING
        kwargs['allowed_filtering'] = self.FILTERING
        return self.transport.set_method('GET').set_pagination(**kwargs).\
            set_ordering(**kwargs).set_filtering(**kwargs).request(**kwargs)

    def getOne(self, _id, c_id, **kwargs):
        """
        Here id is a websites id and c_id is a coupon id

        res = client.CouponsForWebsite.getOne(_id=2, c_id=1)
        res = client.CouponsForWebsite.getOne(2, 1)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['c_id'] = self.sanitize_id(c_id)
        return self.transport.set_method('GET').request(**kwargs)
