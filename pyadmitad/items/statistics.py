from datetime import datetime, date
from pyadmitad.items.base import Item
from pyadmitad.constants import *


__all__ = (
    'StatisticWebsites',
)


class StatisticBase(Item):

    @staticmethod
    def check_date(d):
        s = datetime.strptime(d, DATE_FORMAT).date()
        if s > date.today():
            s = date.today()
        return s.strftime(DATE_FORMAT)

    FILTERING = {
        'date_start': check_date,
        'date_end': check_date,
        'website': int,
        'campaign': int,
        'sub_id': (
            lambda x:
            unicode(x) if len(unicode(x)) <= SUB_ID_MAX_LENGTH else None)
    }


class StatisticWebsites(StatisticBase):
    """
    Statistics by websites

    How to prepare client:

    scope = "statistics"
    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )
    """

    ORDERING = (
        'action',
        'clicks',
        'cr',
        'ctr',
        'ecpc',
        'ecpm',
        'leads',
        'name',
        'payment_sum',
        'payment_sum_approved',
        'payment_sum_declined',
        'payment_sum_open',
        'sales',
        'views',
    )

    def get(self, **kwargs):
        """
        res = client.StatisticWebsites.get()
        res = client.StatisticWebsites.get(website=1, campaign=1)
        res = client.StatisticWebsites.get(sub_id="ADS778")
        res = client.StatisticWebsites.get(limit=2)
        res = client.StatisticWebsites.get(date_start='01.01.2013')

        """
        kwargs['url'] = STATISTIC_WEBSITES_URL
        kwargs['allowed_filtering'] = self.FILTERING
        kwargs['allowed_ordering'] = self.ORDERING
        return self.transport.GET.set_pagination(**kwargs).\
            set_filtering(**kwargs).set_ordering(**kwargs).request(**kwargs)
