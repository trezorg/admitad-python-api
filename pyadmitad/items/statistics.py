from datetime import datetime, date
from pyadmitad.items.base import Item
from pyadmitad.constants import *


__all__ = (
    'StatisticWebsites',
    'StatisticCampaigns',
    'StatisticDays',
    'StatisticMonths',
)


def check_date(d):
    s = datetime.strptime(d, DATE_FORMAT).date()
    if s > date.today():
        s = date.today()
    return s.strftime(DATE_FORMAT)


class StatisticBase(Item):

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

    FILTERING = {
        'date_start': check_date,
        'date_end': check_date,
        'website': int,
        'campaign': int,
        'sub_id': (
            lambda x:
            unicode(x) if len(unicode(x)) <= SUB_ID_MAX_LENGTH else None)
    }

    def get(self, url, **kwargs):
        """Base GET method"""
        kwargs['url'] = url
        kwargs['allowed_filtering'] = self.FILTERING
        kwargs['allowed_ordering'] = self.ORDERING
        return self.transport.GET.set_pagination(**kwargs).\
            set_filtering(**kwargs).set_ordering(**kwargs).request(**kwargs)


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

    def get(self, **kwargs):
        """
        res = client.StatisticWebsites.get()
        res = client.StatisticWebsites.get(website=1, campaign=1)
        res = client.StatisticWebsites.get(sub_id="ADS778")
        res = client.StatisticWebsites.get(limit=2)
        res = client.StatisticWebsites.get(date_start='01.01.2013')

        """
        return super(StatisticWebsites, self).get(
            STATISTIC_WEBSITES_URL, **kwargs)


class StatisticCampaigns(StatisticBase):
    """
    Statistics by campaigns

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

    def get(self, **kwargs):
        """
        res = client.StatisticCampaigns.get()
        res = client.StatisticCampaigns.get(website=1, campaign=1)
        res = client.StatisticCampaigns.get(sub_id="ADS778")
        res = client.StatisticCampaigns.get(limit=2)
        res = client.StatisticCampaigns.get(date_start='01.01.2013')

        """
        return super(StatisticCampaigns, self).get(
            STATISTIC_CAMPAIGNS_URL, **kwargs)


class StatisticDays(StatisticBase):
    """
    Statistics by days

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

    def get(self, **kwargs):
        """
        res = client.StatisticDays.get()
        res = client.StatisticDays.get(website=1, campaign=1)
        res = client.StatisticDays.get(sub_id="ADS778")
        res = client.StatisticDays.get(limit=2)
        res = client.StatisticDays.get(date_start='01.01.2013')
        """
        return super(StatisticDays, self).get(STATISTIC_DAYS_URL, **kwargs)


class StatisticMonths(StatisticBase):
    """
    Statistics by months

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

    def get(self, **kwargs):
        """
        res = client.StatisticMonths.get()
        res = client.StatisticMonths.get(website=1, campaign=1)
        res = client.StatisticMonths.get(sub_id="ADS778")
        res = client.StatisticMonths.get(limit=2)
        res = client.StatisticMonths.get(date_start='01.01.2013')

        """
        return super(StatisticMonths, self).get(STATISTIC_MONTHS_URL, **kwargs)
