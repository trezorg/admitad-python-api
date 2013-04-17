# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import Referrals
from pyadmitad.tests.base import BaseTestCase


class ReferralsTestCase(BaseTestCase):

    def test_get_referrals_request(self):
        self.set_mocker(Referrals.URL, limit=1)
        result = {
            u'_meta': {
                u'count': 2,
                u'limit': 1,
                u'offset': 0
            },
            u'results': [
                {
                    u'id': 8,
                    u'payment': None,
                    u'username': u'username'
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Referrals.get(limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.mocker.verify()

    def test_get_referrals_request_with_id(self):
        self.set_mocker(Referrals.SINGLE_URL, id=8, with_pagination=False)
        result = {
            u'id': 8,
            u'payment': None,
            u'username': u'username'}
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Referrals.getOne(8)
        self.assertEqual(res[u'id'], 8)
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
