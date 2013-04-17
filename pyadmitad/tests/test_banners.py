# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import Banners, BannersForWebsite
from pyadmitad.tests.base import BaseTestCase


class BannersTestCase(BaseTestCase):

    def test_get_banners_request(self):
        self.set_mocker(Banners.URL, id=6, limit=1)
        result = {
            u'_meta': {
                u'count': 5,
                u'limit': 1,
                u'offset': 0
            },
            u'results': [
                {
                    u'banner_image': u'https://admitad.com/media/image.png',
                    u'creation_date': u'2013-01-18 20:13:27',
                    u'flashobj_url': u'',
                    u'id': 1,
                    u'image_url': u'',
                    u'is_flash': False,
                    u'name': u'Gmail Banner',
                    u'size_height': 39,
                    u'size_width': 94,
                    u'traffic_url': u'',
                    u'type': u'jpeg'
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Banners.get(6, limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.mocker.verify()


class BannersForWebsiteTestCase(BaseTestCase):

    def test_get_banners_request(self):
        self.set_mocker(BannersForWebsite.URL, id=6, w_id=22, limit=1)
        result = {
            u'_meta': {
                u'count': 5,
                u'limit': 1,
                u'offset': 0
            },
            u'results': [
                {
                    u'banner_image': u'https://admitad.com/media/image.png',
                    u'creation_date': u'2011-01-13 20:13:27',
                    u'direct_link': u'http://ad.admitad.com/goto/XXXXX/',
                    u'flashobj_url': u'',
                    u'html_code': {
                        u'async': u'see https://www.admitad.com/ru/doc/api/'
                                  u'methods/banners/banners-website/',
                        u'flash': u'see https://www.admitad.com/ru/doc/api/'
                                  u'methods/banners/banners-website/',
                        u'full': u'see https://www.admitad.com/ru/doc/api/'
                                  u'methods/banners/banners-website/',
                        u'image': u'see https://www.admitad.com/ru/doc/api/'
                                 u'methods/banners/banners-website/',
                        u'sync': u'see https://www.admitad.com/ru/doc/api/'
                                  u'methods/banners/banners-website/',
                    },
                    u'id': 1,
                    u'image_url': u'',
                    u'is_flash': False,
                    u'name': u'Gmail Banner',
                    u'size_height': 39,
                    u'size_width': 94,
                    u'traffic_url': u'',
                    u'type': u'jpeg'
                }
            ]
        }

        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.BannersForWebsite.get(6, 22, limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
