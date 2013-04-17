# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import Websites
from pyadmitad.tests.base import BaseTestCase


class WebsitesTestCase(BaseTestCase):

    def test_get_websites_request(self):
        self.set_mocker(Websites.URL, limit=1, offset=2)
        result = {
            u'results': [
                {
                    u'status': u'active',
                    u'kind': u'website',
                    u'is_old': True,
                    u'name': u'site',
                    u'language': None,
                    u'description': u'site',
                    u'verification_code': u'59505879f5',
                    u'creation_date': u'2010-03-31 18:25:19',
                    u'regions': [
                        {
                            u'region': u'RU',
                            u'id': 5
                        }
                    ],
                    u'atnd_visits': 100,
                    u'adservice': None,
                    u'site_url': u'http://www.mail.ru/',
                    u'id': 22,
                    u'categories': [
                        {
                            u'name': u'Категория',
                            u'parent': None,
                            u'id': 5
                        }
                    ],
                    u'atnd_hits': 0
                }
            ],
            u'_meta': {
                u'count': 4,
                u'limit': 1,
                u'offset': 2
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Websites.get(limit=1, offset=2)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.mocker.verify()

    def test_get_websites_request_with_id(self):
        self.set_mocker(Websites.SINGLE_URL, id=22, with_pagination=False)
        result = {
            u'status': u'active',
            u'kind': u'website',
            u'is_old': True,
            u'name': u'site',
            u'language': None,
            u'description': u'site',
            u'verification_code': u'59505879f5',
            u'creation_date': u'2010-03-31 18:25:19',
            u'regions': [
                {
                    u'region': u'RU',
                    u'id': 5
                }
            ],
            u'atnd_visits': 100,
            u'adservice': None,
            u'site_url': u'http://www.mail.ru/',
            u'id': 22,
            u'categories': [
                {
                    u'name': u'Категория',
                    u'parent': None,
                    u'id': 5
                }
            ],
            u'atnd_hits': 0
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Websites.getOne(22)
        self.assertEqual(res[u'id'], 22)
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
