import unittest
from pyadmitad.items import Me
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


if __name__ == '__main__':
    unittest.main()
