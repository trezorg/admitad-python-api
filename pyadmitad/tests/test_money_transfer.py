# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import MoneyTransfers, MoneyTransfersManage
from pyadmitad.tests.base import BaseTestCase


MONEY_TRANSFER_CREATE_DATA = dict(
    currency='USD',
    comment="test",
    recipient="admitadppvweb",
    sum='200.12',
)


class MoneyTransfersTestCase(BaseTestCase):

    def test_get_money_transfers_request(self):
        self.set_mocker(MoneyTransfers.URL, limit=1)
        result = {
            "_meta": {
                "count": 6,
                "limit": 1,
                "offset": 0
            },
            "results": [
                {
                    "comment": "test",
                    "sender": {
                        "username": "webmaster1",
                        "id": 96
                    },
                    "sum": 200.0,
                    "currency": "USD",
                    "date_created": "2013-12-06T12:28:29",
                    "recipient": {
                        "username": "admitadppvweb",
                        "id": 100
                    },
                    "id": 8
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.MoneyTransfers.get(limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.assertEqual(res[u'results'][0][u'currency'], u'USD')
        self.mocker.verify()

    def test_get_money_transfers_request_with_id(self):
        self.set_mocker(MoneyTransfers.SINGLE_URL, id=8, with_pagination=False)
        result = {
            "comment": "test",
            "sender": {
                "username": "webmaster1",
                "id": 96
            },
            "sum": 200.0,
            "currency": "USD",
            "date_created": "2013-12-06T12:28:29",
            "recipient": {
                "username": "admitadppvweb",
                "id": 100
            },
            "id": 8
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.MoneyTransfers.getOne(8)
        self.assertEqual(res[u'id'], 8)
        self.mocker.verify()


class MoneyTransfersManageTestCase(BaseTestCase):

    def test_create_payments_request(self):
        self.set_mocker(MoneyTransfersManage.CREATE_URL,
                        method='POST',
                        with_pagination=False,
                        data=MONEY_TRANSFER_CREATE_DATA)
        result = {
            "comment": "test",
            "sender": {
                "username": "webmaster1",
                "id": 96
            },
            "sum": 200.12,
            "currency": "USD",
            "date_created": "2013-12-06T12:28:29",
            "recipient": {
                "username": "admitadppvweb",
                "id": 100
            },
            "id": 9
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.MoneyTransfersManage.create(
            **MONEY_TRANSFER_CREATE_DATA)
        self.assertEqual(res[u'comment'], u'test')
        self.assertEqual(res[u'currency'], u'USD')
        self.assertEqual(res[u'sum'], 200.12)
        self.assertEqual(res[u'sender'][u'username'], u'webmaster1')
        self.mocker.verify()

if __name__ == '__main__':
    unittest.main()
