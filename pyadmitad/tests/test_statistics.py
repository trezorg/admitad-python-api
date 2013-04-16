# -*- coding: utf-8 -*-

import unittest
from pyadmitad.constants import *
from pyadmitad.items import StatisticWebsites
from pyadmitad.tests.base import BaseTestCase


class StatisticsWebsitesTestCase(BaseTestCase):

    def test_get_statistics_websites_request(self):
        self.set_mocker(
            STATISTIC_WEBSITES_URL,
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


if __name__ == '__main__':
    unittest.main()
