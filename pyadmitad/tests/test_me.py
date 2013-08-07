import unittest
from pyadmitad.items import *
from pyadmitad.tests.base import BaseTestCase


class MeTestCase(BaseTestCase):

    def test_me_request(self):
        self.set_mocker(Me.URL, with_pagination=False)
        result = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'id': 1,
            'language': 'ru'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Me.get()
        self.assertEqual(res['username'], 'username')
        self.assertEqual(res['first_name'], 'first_name')
        self.assertEqual(res['id'], 1)
        self.assertEqual(res['language'], 'ru')
        self.mocker.verify()


class BalanceTestCase(BaseTestCase):

    def test_balance_request(self):
        self.set_mocker(Balance.URL, with_pagination=False)
        result = [
            {
                'currency': 'USD',
                'balance': '20000.00'
            },
            {
                'currency': 'EUR',
                'balance': '0.00'
            },
            {
                'currency': 'RUB',
                'balance': '0.00'
            }
        ]
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Balance.get()
        self.assertEqual(len(res), 3)
        self.assertIn('balance', res[0])
        self.assertIn('currency', res[0])
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
