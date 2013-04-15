import unittest
from mocker import MockerTestCase
from pyadmitad.api import get_oauth_client
from pyadmitad.constants import *
from pyadmitad.transport import build_headers


class MeTestCase(MockerTestCase):

    def test_me_request(self):
        access_token = 'access_token'
        client = get_oauth_client(access_token)
        obj = self.mocker.patch(client.transport)
        url = ME_URL
        kwargs = {
            'data': None,
            'headers': build_headers(access_token),
            'method': 'GET'
        }
        obj.api_request(url, **kwargs)
        result = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'id': 1,
            'language': 'ru'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = client.Me.get()
        self.assertEqual(res['username'], 'username')
        self.assertEqual(res['first_name'], 'first_name')
        self.assertEqual(res['id'], 1)
        self.assertEqual(res['language'], 'ru')
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
