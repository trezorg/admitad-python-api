from pyadmitad.items.base import Item
from pyadmitad.constants import *


__all__ = (
    'Coupons',
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

    ORDERING = ('name', 'date_start', 'date_end', 'name',)
    FILTERING = {
        'campaign': int,
        'campaign_category': int,
        'category': int,
        'type': int
    }

    def get(self, **kwargs):
        """
        print client.Coupons.get()
        print client.Coupons.get(order_by=date_start)
        print client.Coupons.get(order_by=-date_end)
        print client.Coupons.get(campaign=1, category=2)

        If you want to filter by many values of same key:
            on example - campaign=1, campaign=2:

            use "filtering" parameter: filtering={'campaign': [1, 2]}

        print client.Coupons.get(filtering={'campaign': [1, 2]}, category=2)

        """
        kwargs['url'] = COUPONS_URL
        kwargs['allowed_ordering'] = self.ORDERING
        kwargs['allowed_filtering'] = self.FILTERING
        return self.transport.GET.set_pagination(**kwargs).\
            set_ordering(**kwargs).set_filtering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        print client.Coupons.getOne(_id=2)
        print client.Coupons.getOne(2)
        """
        kwargs['url'] = COUPONS_SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.GET.request(**kwargs)
