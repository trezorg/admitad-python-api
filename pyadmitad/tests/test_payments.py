# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import Payments, PaymentsManage
from pyadmitad.tests.base import BaseTestCase


class PaymentsTestCase(BaseTestCase):

    def test_get_payments_request(self):
        self.set_mocker(Payments.URL, limit=1)
        result = {
            u'_meta': {
                u'count': 6,
                u'limit': 1,
                u'offset': 0
            },
            u'results': [
                {
                    u'comment': u'',
                    u'currency': u'USD',
                    u'datetime': u'2012-05-27 19:45:07',
                    u'id': 68,
                    u'payment_sum': u'2000.00',
                    u'status': u'pending',
                    u'withdrawal_type': u'webmoney'
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Payments.get(limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.assertEqual(res[u'results'][0][u'currency'], u'USD')
        self.mocker.verify()

    def test_get_payments_request_with_id(self):
        self.set_mocker(Payments.SINGLE_URL, id=68, with_pagination=False)
        result = {
            u'comment': u'',
            u'currency': u'USD',
            u'datetime': u'2012-05-27 19:45:07',
            u'id': 68,
            u'payment_sum': u'2000.00',
            u'status': u'pending',
            u'withdrawal_type': u'webmoney'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Payments.getOne(68)
        self.assertEqual(res[u'id'], 68)
        self.mocker.verify()


class PaymentsManageTestCase(BaseTestCase):

    def test_create_payments_request(self):
        self.set_mocker(PaymentsManage.CREATE_URL,
                        method='POST', with_pagination=False, code='EUR')
        result = {
            u'comment': u'',
            u'currency': u'EUR',
            u'datetime': u'2013-04-24 15:07:47',
            u'id': 71,
            u'payment_sum': u'10000',
            u'status': u'draft',
            u'withdrawal_type': u''
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.PaymentsManage.create('EUR')
        self.assertEqual(res[u'status'], u'draft')
        self.assertEqual(res[u'currency'], u'EUR')
        self.assertEqual(res[u'id'], 71)
        self.mocker.verify()

    def test_confirm_payments_request(self):
        self.set_mocker(PaymentsManage.CONFIRM_URL,
                        method='POST', with_pagination=False, id=71)
        result = {
            u'comment': u'',
            u'currency': u'EUR',
            u'datetime': u'2013-04-24 15:07:47',
            u'id': 71,
            u'payment_sum': u'10000.00',
            u'status': u'pending',
            u'withdrawal_type': u'webmoney'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.PaymentsManage.confirm(71)
        self.assertEqual(res[u'status'], u'pending')
        self.assertEqual(res[u'currency'], u'EUR')
        self.assertEqual(res[u'id'], 71)
        self.mocker.verify()

    def test_delete_payments_request(self):
        self.set_mocker(PaymentsManage.DELETE_URL,
                        method='POST', with_pagination=False, id=71)
        result = {
            u'message': u'Заявка удалена успешно.',
            u'success': u'Deleted'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.PaymentsManage.delete(71)
        self.assertIn('success', res)
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
