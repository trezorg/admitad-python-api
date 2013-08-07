# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import StatisticWebsites, StatisticCampaigns,\
    StatisticDays, StatisticMonths, StatisticActions, StatisticSubIds,\
    StatisticSources, StatisticKeywords
from pyadmitad.tests.base import BaseTestCase


class StatisticsWebsitesTestCase(BaseTestCase):

    def test_get_statistics_websites_request(self):
        self.set_mocker(
            StatisticWebsites.URL,
            website=22,
            allowed_filtering=StatisticWebsites.FILTERING,
            allowed_ordering=StatisticWebsites.ORDERING
        )
        result = {
            u'results': [
                {
                    u'clicks': 184,
                    u'cr': 0.3,
                    u'ctr': 0.03,
                    u'currency': u'RUB',
                    u'ecpc': 124.77,
                    u'ecpm': 4403.26,
                    u'leads_sum': 61,
                    u'payment_sum_approved': 1870.67,
                    u'payment_sum_declined': 0.0,
                    u'payment_sum_open': 21087.97,
                    u'sales_sum': 10,
                    u'views': 5214,
                    u'website_id': 22,
                    u'website_name': u'website'
                }
            ],
            u'_meta': {
                u'count': 1,
                u'limit': 20,
                u'offset': 0
            },
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.StatisticWebsites.get(website=22)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'results'][0][u'website_id'], 22)
        self.mocker.verify()


class StatisticsCampaignTestCase(BaseTestCase):

    def test_get_statistics_campaign_request(self):
        self.set_mocker(
            StatisticCampaigns.URL,
            campaign=9,
            allowed_filtering=StatisticCampaigns.FILTERING,
            allowed_ordering=StatisticCampaigns.ORDERING
        )
        result = {
            u'results': [
                {
                    u'advcampaign_id': 9,
                    u'advcampaign_name': u'Campaign',
                    u'clicks': 35,
                    u'cr': 0.1143,
                    u'ctr': 0.4487,
                    u'currency': u'RUB',
                    u'ecpc': 5.714286,
                    u'ecpm': 2564.102564,
                    u'leads_sum': 4,
                    u'payment_sum_approved': 0.0,
                    u'payment_sum_declined': 0.0,
                    u'payment_sum_open': 200.0,
                    u'sales_sum': 0,
                    u'views': 78
                },
            ],
            u'_meta': {
                u'count': 1,
                u'limit': 20,
                u'offset': 0
            },
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.StatisticCampaigns.get(campaign=9)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'results'][0][u'advcampaign_id'], 9)
        self.mocker.verify()


class StatisticsDaysTestCase(BaseTestCase):

    def test_get_statistics_days_request(self):
        self.set_mocker(
            StatisticDays.URL,
            campaign=9,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1,
            allowed_filtering=StatisticDays.FILTERING,
            allowed_ordering=StatisticDays.ORDERING
        )
        result = {
            u'results': [
                {
                    u'clicks': 3,
                    u'cr': 0.3333,
                    u'ctr': 0.0,
                    u'currency': u'RUB',
                    u'date': u'2013-01-12',
                    u'ecpc': 27.88,
                    u'ecpm': 0.0,
                    u'leads_sum': 1,
                    u'payment_sum_approved': 83.65,
                    u'payment_sum_declined': 0.0,
                    u'payment_sum_open': 0.0,
                    u'sales_sum': 0,
                    u'views': 0
                }
            ],
            u'_meta': {
                u'count': 3,
                u'limit': 1,
                u'offset': 0
            },
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.StatisticDays.get(
            campaign=9,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1
        )
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()


class StatisticsMonthsTestCase(BaseTestCase):

    def test_get_statistics_months_request(self):
        self.set_mocker(
            StatisticMonths.URL,
            campaign=9,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1,
            allowed_filtering=StatisticMonths.FILTERING,
            allowed_ordering=StatisticMonths.ORDERING
        )
        result = {
            u'results': [
                {
                    u'clicks': 3,
                    u'cr': 0.3333,
                    u'ctr': 0.0,
                    u'currency': u'RUB',
                    u'date': u'2013-01-12',
                    u'ecpc': 27.88,
                    u'ecpm': 0.0,
                    u'leads_sum': 1,
                    u'payment_sum_approved': 83.65,
                    u'payment_sum_declined': 0.0,
                    u'payment_sum_open': 0.0,
                    u'sales_sum': 0,
                    u'views': 0
                }
            ],
            u'_meta': {
                u'count': 3,
                u'limit': 1,
                u'offset': 0
            },
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.StatisticMonths.get(
            campaign=9,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1
        )
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()


class StatisticsActionsTestCase(BaseTestCase):

    def test_get_statistics_actions_request(self):
        self.set_mocker(
            StatisticActions.URL,
            campaign=9,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1,
            allowed_filtering=StatisticActions.FILTERING,
            allowed_ordering=StatisticActions.ORDERING
        )
        result = {
            u'results': [
                {
                    u'action': u'action name',
                    u'action_date': u'2013-01-15 18:23:54',
                    u'action_id': 281,
                    u'advcampaign_id': 9,
                    u'advcampaign_name': u'Campaign',
                    u'cart': 777.0,
                    u'click_date': u'2011-01-13 18:23:50',
                    u'closing_date': u'2012-04-02',
                    u'status_updated': u'2011-09-16 23:13:35',
                    u'comment': None,
                    u'conversion_time': 4,
                    u'currency': u'RUB',
                    u'keyword': None,
                    u'payment': 50.0,
                    u'status': u'pending',
                    u'subid': None,
                    u'subid1': None,
                    u'subid2': None,
                    u'subid3': None,
                    u'subid4': None,
                    u'website_name': u'site1_of_webmaster1'
                }
            ],
            u'_meta': {
                u'count': 89,
                u'limit': 1,
                u'offset': 0
            },
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.StatisticActions.get(
            campaign=9,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1
        )
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()


class StatisticsSubIdsTestCase(BaseTestCase):

    def test_get_statistics_sub_ids_request(self):
        self.set_mocker(
            StatisticSubIds.URL % '',
            campaign=9,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1,
            allowed_filtering=StatisticSubIds.FILTERING,
            allowed_ordering=StatisticSubIds.ORDERING
        )
        result = {
            u'_meta': {
                u'count': 1,
                u'limit': 1,
                u'offset': 0
            },
            u'results': [
                {
                    u'clicks': 1,
                    u'cr': 89.0,
                    u'currency': u'RUB',
                    u'ecpc': 5202.5,
                    u'leads_sum': 89,
                    u'payment_sum_approved': 5002.5,
                    u'payment_sum_declined': 0.0,
                    u'payment_sum_open': 200.0,
                    u'sales_sum': 0,
                    u'subid': u'sub'
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.StatisticSubIds.get(
            campaign=9,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1
        )
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()


class StatisticsSourcesTestCase(BaseTestCase):

    def test_get_statistics_sources_request(self):
        self.set_mocker(
            StatisticSources.URL,
            campaign=6,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1,
            allowed_filtering=StatisticSources.FILTERING,
            allowed_ordering=StatisticSources.ORDERING
        )
        result = {
            u'_meta': {
                u'count': 2,
                u'limit': 1,
                u'offset': 0
            },
            u'results': [
                {
                    u'clicks': 7,
                    u'cr': 0.1429,
                    u'currency': u'RUB',
                    u'ecpc': 51.785714,
                    u'leads_sum': 1,
                    u'payment_sum_approved': 0.0,
                    u'payment_sum_declined': 0.0,
                    u'payment_sum_open': 362.5,
                    u'sales_sum': 0,
                    u'source': u'g',
                    u'source_name': u'Google Adwords'
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.StatisticSources.get(
            campaign=6,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1
        )
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()


class StatisticsKeywordsTestCase(BaseTestCase):

    def test_get_statistics_keywords_request(self):
        self.set_mocker(
            StatisticKeywords.URL,
            campaign=6,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1,
            allowed_filtering=StatisticKeywords.FILTERING,
            allowed_ordering=StatisticKeywords.ORDERING
        )
        result = {
            u'_meta': {
                u'count': 3,
                u'limit': 1,
                u'offset': 0
            },
            u'results': [
                {
                    u'clicks': 2,
                    u'cr': 0.0,
                    u'currency': u'RUB',
                    u'ecpc': 0.0,
                    u'keyword': u'keyword',
                    u'leads_sum': 0,
                    u'payment_sum_approved': 0.0,
                    u'payment_sum_declined': 0.0,
                    u'payment_sum_open': 0.0,
                    u'sales_sum': 0
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.StatisticKeywords.get(
            campaign=6,
            date_start='01.01.2013',
            date_end='01.31.2013',
            limit=1
        )
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
