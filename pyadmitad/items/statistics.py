from datetime import datetime, date
from pyadmitad.items.base import Item
from pyadmitad.constants import *


__all__ = (
    'StatisticWebsites',
    'StatisticCampaigns',
    'StatisticDays',
    'StatisticMonths',
    'StatisticActions',
    'StatisticSubIds',
    'StatisticSources',
    'StatisticKeywords',
)


def check_date(d):
    s = datetime.strptime(d, DATE_FORMAT).date()
    if s > date.today():
        s = date.today()
    return s.strftime(DATE_FORMAT)


class StatisticBase(Item):

    STATUSES = (1, 2, 3)
    SOURCES = ('g', 'y')
    ACTION_TYPES = ('lead', 'Lead')

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


class StatisticActions(StatisticBase):
    """
    Statistics by actions

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
        'banner',
        'banner_id',
        'campaign',
        'cart',
        'click_date',
        'conv_time',
        'datetime',
        'payment',
        'status',
        'subid',
        'website'
    )

    FILTERING = {
        'date_start': check_date,
        'date_end': check_date,
        'website': int,
        'campaign': int,
        'sub_id': (
            lambda x:
            unicode(x) if len(unicode(x)) <= SUB_ID_MAX_LENGTH else None),
        'source': (
            lambda x: x if x in StatisticBase.SOURCES else None),
        'status': (
            lambda x: x if x in StatisticBase.STATUSES else None),
        'keyword': unicode,
        'action': unicode,
        'action_type': (
            lambda x: x if x in StatisticActions.ACTION_TYPES else None),
    }

    def get(self, **kwargs):
        """
        res = client.StatisticActions.get()
        res = client.StatisticActions.get(website=1, campaign=1)
        res = client.StatisticActions.get(sub_id="ADS778")
        res = client.StatisticActions.get(limit=2)
        res = client.StatisticActions.get(date_start='01.01.2013')

        """
        return super(StatisticActions, self).get(
            STATISTIC_ACTIONS_URL, **kwargs)


class StatisticSubIds(StatisticBase):
    """
    Statistics by sub-ids

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
        'actions',
        'clicks',
        'cr',
        'ecpc',
        'leads',
        'payment_sum',
        'payment_sum_approved',
        'payment_sum_declined',
        'payment_sum_open',
        'sales',
        'subid',
    )

    FILTERING = {
        'date_start': check_date,
        'date_end': check_date,
        'website': int,
        'campaign': int,
    }

    def get(self, **kwargs):
        """
        res = client.StatisticSubIds.get()
        res = client.StatisticSubIds.get(date_start='01.01.2013')
        res = client.StatisticSubIds.get(sub_id="ADS778")
        res = client.StatisticSubIds.get(limit=2)

        """
        return super(StatisticSubIds, self).get(STATISTIC_SUB_IDS_URL, **kwargs)


class StatisticSources(StatisticBase):
    """
    Statistics by sources

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
        'actions',
        'clicks',
        'cr',
        'ecpc',
        'leads',
        'payment_sum',
        'payment_sum_approved',
        'payment_sum_declined',
        'payment_sum_open',
        'sales',
        'source',
    )

    FILTERING = {
        'date_start': check_date,
        'date_end': check_date,
        'website': int,
        'campaign': int,
    }

    def get(self, **kwargs):
        """
        res = client.StatisticSources.get()
        res = client.StatisticSources.get(date_start='01.01.2013')
        res = client.StatisticSources.get(limit=2)

        """
        return super(StatisticSources, self).get(
            STATISTIC_SOURCES_URL, **kwargs)


class StatisticKeywords(StatisticBase):
    """
    Statistics by keywords

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
        'actions',
        'clicks',
        'cr',
        'ecpc',
        'keyword',
        'leads',
        'payment_sum',
        'payment_sum_approved',
        'payment_sum_declined',
        'payment_sum_open',
        'sales',
        'source',
    )

    FILTERING = {
        'date_start': check_date,
        'date_end': check_date,
        'website': int,
        'campaign': int,
        'source': (
            lambda x: x if x in StatisticBase.SOURCES else None),
    }

    def get(self, **kwargs):
        """
        res = client.StatisticKeywords.get()
        res = client.StatisticKeywords.get(date_start='01.01.2013')
        res = client.StatisticKeywords.get(limit=2)

        """
        return super(StatisticKeywords, self).get(
            STATISTIC_KEYWORDS_URL, **kwargs)
