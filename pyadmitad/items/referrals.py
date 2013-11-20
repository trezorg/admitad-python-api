from pyadmitad.items.base import Item


__all__ = (
    'Referrals',
)


class Referrals(Item):
    """
    List of referrals

    Required scope - "referrals"
    """

    URL = Item.prepare_url('referrals')
    SINGLE_URL = Item.prepare_url('referrals/%(id)s')

    FILTERING = {
        'date_start': Item.check_date,
        'date_end': Item.check_date
    }

    def get(self, **kwargs):
        """
        res = client.Referrals.get()
        res = client.Referrals.get(limit=2)
        """
        kwargs['url'] = self.URL
        kwargs['allowed_filtering'] = self.FILTERING
        return self.transport.set_method('GET').set_pagination(**kwargs).\
            set_filtering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        res = client.Referrals.getOne(_id=2)
        res = client.Referrals.getOne(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('GET').request(**kwargs)
