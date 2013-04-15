from pyadmitad.items.base import Item
from pyadmitad.constants import *


__all__ = (
    'Coupons',
    'CouponsForWebsite',
)


class Coupons(Item):
    """
    List of coupons

    How to prepare client:

    scope = "coupons"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """

    ORDERING = ('name', 'date_start', 'date_end', 'rating',)
    FILTERING = {
        'campaign': int,
        'campaign_category': int,
        'category': int,
        'type': int
    }

    def get(self, **kwargs):
        """
        res = client.Coupons.get()
        res = client.Coupons.get(order_by=date_start)
        res = client.Coupons.get(order_by=-date_end)
        res = client.Coupons.get(campaign=1, category=2)

        If you want to filter by many values of the same key:
            on example - campaign=1, campaign=2:

            use "filtering" parameter: filtering={'campaign': [1, 2]}

        res = client.Coupons.get(filtering={'campaign': [1, 2]}, category=2)

        """
        kwargs['url'] = COUPONS_URL
        kwargs['allowed_ordering'] = self.ORDERING
        kwargs['allowed_filtering'] = self.FILTERING
        return self.transport.GET.set_pagination(**kwargs).\
            set_ordering(**kwargs).set_filtering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        res = client.Coupons.getOne(_id=2)
        res = client.Coupons.getOne(2)
        """
        kwargs['url'] = COUPONS_SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.GET.request(**kwargs)


class CouponsForWebsite(Item):
    """
    List of the website coupons

    How to prepare client:

    scope = "coupons_for_website"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """

    ORDERING = ('name', 'date_start', 'date_end', 'rating',)
    FILTERING = {
        'campaign': int,
        'campaign_category': int,
        'category': int,
        'type': int
    }

    def get(self, _id, **kwargs):
        """
        res = client.CouponsForWebsite.get(_id=2)
        res = client.CouponsForWebsite.get(2)
        res = client.CouponsForWebsite.get(2, order_by=date_start)
        res = client.CouponsForWebsite.get(2, campaign=1, category=2)

        If you want to filter by many values of the same key:
            on example - campaign=1, campaign=2:

            use "filtering" parameter: filtering={'campaign': [1, 2]}

        res = client.CouponsForWebsite.get(
            2, filtering={'campaign': [1, 2]}, category=2)

        """
        kwargs['url'] = COUPONS_WEBSITE_URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['allowed_ordering'] = self.ORDERING
        kwargs['allowed_filtering'] = self.FILTERING
        return self.transport.GET.set_pagination(**kwargs).\
            set_ordering(**kwargs).set_filtering(**kwargs).request(**kwargs)

    def getOne(self, _id, c_id, **kwargs):
        """
        res = client.CouponsForWebsite.getOne(_id=2, c_id=1)
        res = client.CouponsForWebsite.getOne(2, 1)
        """
        kwargs['url'] = COUPONS_WEBSITE_SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['c_id'] = self.sanitize_id(c_id)
        return self.transport.GET.request(**kwargs)
