# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import Coupons, CouponsForWebsite
from pyadmitad.tests.base import BaseTestCase


class CouponsTestCase(BaseTestCase):

    def test_get_coupons_request(self):
        self.set_mocker(Coupons.URL, limit=1)
        result = {
            u'results': [
                {
                    u'campaign': {
                        u'id': 8,
                        u'name': u'AdvCamp 3'
                    },
                    u'categories': [
                        {
                            u'id': 1,
                            u'name': u'Детские товары'
                        },
                        {
                            u'id': 3,
                            u'name': u'Мода & аксессуары'
                        },
                        {
                            u'id': 4,
                            u'name': u'Обувь женская & мужская'
                        }
                    ],
                    u'date_end': u'2013-05-10 23:59:59',
                    u'date_start': u'2011-11-02 00:00:00',
                    u'description': u'',
                    u'exclusive': False,
                    u'id': 1,
                    u'image': u'https://admitad.com/media/path_img.png',
                    u'name': u'Купон',
                    u'rating': u'0.00',
                    u'short_name': u'coupon',
                    u'species': u'promocode',
                    u'status': u'active',
                    u'types': [
                        {
                            u'id': 1,
                            u'name': u'Бесплатная доставка'
                        }
                    ]
                }
            ],
            u'_meta': {
                u'count': 6,
                u'limit': 1,
                u'offset': 0
            },
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Coupons.get(limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.mocker.verify()

    def test_get_coupons_request_with_id(self):
        self.set_mocker(Coupons.SINGLE_URL, id=1, with_pagination=False)
        result = {
            u'campaign': {
                u'id': 8,
                u'name': u'AdvCamp 3'
            },
            u'categories': [
                {
                    u'id': 1,
                    u'name': u'Детские товары'
                },
                {
                    u'id': 3,
                    u'name': u'Мода & аксессуары'
                },
                {
                    u'id': 4,
                    u'name': u'Обувь женская & мужская'
                }
            ],
            u'date_end': u'2013-05-10 23:59:59',
            u'date_start': u'2011-11-02 00:00:00',
            u'description': u'',
            u'exclusive': False,
            u'id': 1,
            u'image': u'https://admitad.com/media/path_img.png',
            u'name': u'Купон',
            u'rating': u'0.00',
            u'short_name': u'coupon',
            u'species': u'promocode',
            u'status': u'active',
            u'types': [
                {
                    u'id': 1,
                    u'name': u'Бесплатная доставка'
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Coupons.getOne(1)
        self.assertEqual(res[u'id'], 1)
        self.mocker.verify()


class CouponsForWebsiteTestCase(BaseTestCase):

    def test_get_coupons_for_website_request(self):
        self.set_mocker(CouponsForWebsite.URL, id=3, limit=1)
        result = {
            u'results': [
                {
                    u'campaign': {
                        u'id': 8,
                        u'name': u'AdvCamp 3'
                    },
                    u'categories': [
                        {
                            u'id': 1,
                            u'name': u'Детские товары'
                        },
                        {
                            u'id': 3,
                            u'name': u'Мода & аксессуары'
                        },
                        {
                            u'id': 4,
                            u'name': u'Обувь женская & мужская'
                        }
                    ],
                    u'date_end': u'2013-05-10 23:59:59',
                    u'date_start': u'2011-11-02 00:00:00',
                    u'description': u'',
                    u'exclusive': False,
                    u'id': 1,
                    u'image': u'https://admitad.com/media/path_img.png',
                    u'name': u'Купон',
                    u'rating': u'0.00',
                    u'short_name': u'coupon',
                    u'species': u'promocode',
                    u'status': u'active',
                    u'types': [
                        {
                            u'id': 1,
                            u'name': u'Бесплатная доставка'
                        }
                    ]
                }
            ],
            u'_meta': {
                u'count': 6,
                u'limit': 1,
                u'offset': 0
            },
            }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.CouponsForWebsite.get(_id=3, limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.mocker.verify()

    def test_get_coupons_for_website_request_with_id(self):
        self.set_mocker(
            CouponsForWebsite.SINGLE_URL, id=3, c_id=1, with_pagination=False)
        result = {
            u'campaign': {
                u'id': 8,
                u'name': u'AdvCamp 3'
            },
            u'categories': [
                {
                    u'id': 1,
                    u'name': u'Детские товары'
                },
                {
                    u'id': 3,
                    u'name': u'Мода & аксессуары'
                },
                {
                    u'id': 4,
                    u'name': u'Обувь женская & мужская'
                }
            ],
            u'date_end': u'2013-05-10 23:59:59',
            u'date_start': u'2011-11-02 00:00:00',
            u'description': u'',
            u'exclusive': False,
            u'id': 1,
            u'image': u'https://admitad.com/media/path_img.png',
            u'name': u'Купон',
            u'rating': u'0.00',
            u'short_name': u'coupon',
            u'species': u'promocode',
            u'status': u'active',
            u'types': [
                {
                    u'id': 1,
                    u'name': u'Бесплатная доставка'
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.CouponsForWebsite.getOne(3, 1)
        self.assertEqual(res[u'id'], 1)
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
