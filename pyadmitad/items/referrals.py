from pyadmitad.items.base import Item
from pyadmitad.constants import *


__all__ = (
    'Referrals',
)


class Referrals(Item):
    """
    List of referrals

    How to prepare client:

    scope = "referrals"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """

    FILTERING = {
        'date_start': Item.check_date,
        'date_end': Item.check_date
    }

    def get(self, **kwargs):
        """
        res = client.Referrals.get()
        res = client.Referrals.get(limit=2)
        """
        kwargs['url'] = REFERRALS_URL
        kwargs['allowed_filtering'] = self.FILTERING
        return self.transport.GET.set_pagination(**kwargs).\
            set_filtering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        res = client.Referrals.getOne(_id=2)
        res = client.Referrals.getOne(2)
        """
        kwargs['url'] = REFERRALS_SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.GET.request(**kwargs)
