from copy import copy
from pyadmitad.constants import SUB_ID_MAX_LENGTH
from pyadmitad.items.base import Item


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

    @staticmethod
    def check_sub_id(sub_id):
        return u'%s' % sub_id if len(sub_id) <= SUB_ID_MAX_LENGTH else None

    @staticmethod
    def check_sources(source):
        return source if source in StatisticBase.SOURCES else None,

    @staticmethod
    def check_status(status):
        return status if status in StatisticBase.STATUSES else None,

    @staticmethod
    def check_actions_type(action_type):
        return action_type if action_type\
            in StatisticBase.ACTION_TYPES else None,

    FILTERING = {
        'date_start': Item.check_date,
        'date_end': Item.check_date,
        'website': int,
        'campaign': int,
        'subid': check_sub_id
    }

    def get(self, url, **kwargs):
        """Base GET method"""
        kwargs['url'] = url
        kwargs['allowed_filtering'] = self.FILTERING
        kwargs['allowed_ordering'] = self.ORDERING
        return self.transport.set_method('GET').set_pagination(**kwargs).\
            set_filtering(**kwargs).set_ordering(**kwargs).request(**kwargs)


class StatisticWebsites(StatisticBase):
    """
    Statistics by websites

    Required scope - "statistics"
    """

    URL = Item.prepare_url('statistics/websites')

    def get(self, **kwargs):
        """
        res = client.StatisticWebsites.get()
        res = client.StatisticWebsites.get(website=1, campaign=1)
        res = client.StatisticWebsites.get(subid="ADS778")
        res = client.StatisticWebsites.get(limit=2)
        res = client.StatisticWebsites.get(date_start='01.01.2013')

        """
        return super(StatisticWebsites, self).get(self.URL, **kwargs)


class StatisticCampaigns(StatisticBase):
    """
    Statistics by campaigns

    Required scope - "statistics"
    """

    URL = Item.prepare_url('statistics/campaigns')

    def get(self, **kwargs):
        """
        res = client.StatisticCampaigns.get()
        res = client.StatisticCampaigns.get(website=1, campaign=1)
        res = client.StatisticCampaigns.get(sub_id="ADS778")
        res = client.StatisticCampaigns.get(limit=2)
        res = client.StatisticCampaigns.get(date_start='01.01.2013')

        """
        return super(StatisticCampaigns, self).get(self.URL, **kwargs)


class StatisticDays(StatisticBase):
    """
    Statistics by days

    Required scope - "statistics"
    """

    URL = Item.prepare_url('statistics/dates')

    def get(self, **kwargs):
        """
        res = client.StatisticDays.get()
        res = client.StatisticDays.get(website=1, campaign=1)
        res = client.StatisticDays.get(sub_id="ADS778")
        res = client.StatisticDays.get(limit=2)
        res = client.StatisticDays.get(date_start='01.01.2013')
        """
        return super(StatisticDays, self).get(self.URL, **kwargs)


class StatisticMonths(StatisticBase):
    """
    Statistics by months

    Required scope - "statistics"
    """

    URL = Item.prepare_url('statistics/months')

    def get(self, **kwargs):
        """
        res = client.StatisticMonths.get()
        res = client.StatisticMonths.get(website=1, campaign=1)
        res = client.StatisticMonths.get(sub_id="ADS778")
        res = client.StatisticMonths.get(limit=2)
        res = client.StatisticMonths.get(date_start='01.01.2013')

        """
        return super(StatisticMonths, self).get(self.URL, **kwargs)


class StatisticActions(StatisticBase):
    """
    Statistics by actions

    Required scope - "statistics"
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
        'subid1',
        'subid2',
        'subid3',
        'subid4',
        'website'
    )

    FILTERING = {
        'date_start': Item.check_date,
        'date_end': Item.check_date,
        'closing_date_start': Item.check_date,
        'closing_date_end': Item.check_date,
        'status_updated_start': Item.check_long_date,
        'status_updated_end': Item.check_long_date,
        'website': int,
        'campaign': int,
        'subid': StatisticBase.check_sub_id,
        'subid1': StatisticBase.check_sub_id,
        'subid2': StatisticBase.check_sub_id,
        'subid3': StatisticBase.check_sub_id,
        'subid4': StatisticBase.check_sub_id,
        'source': StatisticBase.check_sources,
        'status': StatisticBase.check_status,
        'keyword': Item.to_unicode,
        'action': Item.to_unicode,
        'action_type': StatisticBase.check_actions_type,
        'action_id': int
    }

    URL = Item.prepare_url('statistics/actions')

    def get(self, **kwargs):
        """
        res = client.StatisticActions.get()
        res = client.StatisticActions.get(website=1, campaign=1)
        res = client.StatisticActions.get(subid="ADS778")
        res = client.StatisticActions.get(limit=2)
        res = client.StatisticActions.get(date_start='01.01.2013')

        """
        return super(StatisticActions, self).get(self.URL, **kwargs)


class StatisticSubIds(StatisticBase):
    """
    Statistics by sub-ids

    Required scope - "statistics"
    """
    SUB_ID_NUMBERS = range(0, 5)

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
        'sales'
    )

    FILTERING = {
        'date_start': Item.check_date,
        'date_end': Item.check_date,
        'website': int,
        'campaign': int,
    }

    URL = Item.prepare_url('statistics/sub_ids%s')

    def sanitize_sub_id_number(self, number):
        if number not in self.SUB_ID_NUMBERS:
            raise ValueError("Invalid subid number. '%s': %s" % (
                number, self.SUB_ID_NUMBERS))

    def prepare_filtering(self, sub_id_number):
        params = copy(self.FILTERING)
        subid_params = dict([
            ('subid%s' % (val or ''), StatisticBase.check_sub_id)
            for val in self.SUB_ID_NUMBERS if val != sub_id_number])
        params.update(subid_params)
        return params

    def prepare_ordering(self, sub_id_number):
        sub_id_name = 'subid%s' % (sub_id_number or '')
        return self.ORDERING + (sub_id_name,)

    def get(self, sub_id_number=0, **kwargs):
        """
        Here sub_id_number is subid number.
        It is allowed from 0 to 5 excluding.
        It just will send request to sub_ids, sub_ids1, sub_ids2,
         sub_ids3, sub_ids4 urls correspondingly.

        res = client.StatisticSubIds.get()
        res = client.StatisticSubIds.get(date_start='01.01.2013')
        res = client.StatisticSubIds.get(subid="ADS778")
        res = client.StatisticSubIds.get(subid1="ADS778", sub_id_number=2)
        res = client.StatisticSubIds.get(limit=2)

        """
        self.sanitize_sub_id_number(sub_id_number)
        kwargs['url'] = self.URL % (sub_id_number or '')
        kwargs['allowed_filtering'] = self.prepare_filtering(sub_id_number)
        kwargs['allowed_ordering'] = self.prepare_ordering(sub_id_number)
        return self.transport.set_method('GET').set_pagination(**kwargs).\
            set_filtering(**kwargs).set_ordering(**kwargs).request(**kwargs)


class StatisticSources(StatisticBase):
    """
    Statistics by sources

    Required scope - "statistics"
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
        'date_start': Item.check_date,
        'date_end': Item.check_date,
        'website': int,
        'campaign': int,
    }

    URL = Item.prepare_url('statistics/sources')

    def get(self, **kwargs):
        """
        res = client.StatisticSources.get()
        res = client.StatisticSources.get(date_start='01.01.2013')
        res = client.StatisticSources.get(limit=2)

        """
        return super(StatisticSources, self).get(self.URL, **kwargs)


class StatisticKeywords(StatisticBase):
    """
    Statistics by keywords

    Required scope - "statistics"
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
        'date_start': Item.check_date,
        'date_end': Item.check_date,
        'website': int,
        'campaign': int,
        'source': (
            lambda x: x if x in StatisticBase.SOURCES else None),
    }

    URL = Item.prepare_url('statistics/keywords')

    def get(self, **kwargs):
        """
        res = client.StatisticKeywords.get()
        res = client.StatisticKeywords.get(date_start='01.01.2013')
        res = client.StatisticKeywords.get(limit=2)

        """
        return super(StatisticKeywords, self).get(self.URL, **kwargs)
