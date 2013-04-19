# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import ProductVendors, ProductCategories,\
    ProductCampaigns, Products
from pyadmitad.tests.base import BaseTestCase


PRODUCTS_RESULT = {
    u'_meta': {
        u'count': 156,
        u'limit': 1,
        u'offset': 1
    },
    u'results': [
        {
            u'advcampaign': {
                u'id': 6,
                u'name': u'AdvCamp 1'
            },
            u'available': True,
            u'category': {
                u'id': 3,
                u'name': u'category-child1'
            },
            u'currency': u'RUB',
            u'description': None,
            u'id': 2,
            u'model': u'JAISALMER',
            u'name': u'Свеча ароматическая Comme des Garcons',
            u'param': {
                u'Пол': u'Уни',
                u'Размер': u'145 гр.'
            },
            u'picture': u'http://cdn.admitad.com/some_file.jpg',
            u'picture_orig': u'http://content.some/path/file.jpg',
            u'price': 3900.0,
            u'thumbnail': u'http://cdn.admitad.com/some_file.jpg',
            u'typePrefix': u'Свеча ароматическая',
            u'updated': u'2012-08-30 21:35:26',
            u'url': u'http://ad.admitad.com/goto/'
                    u'195b832b828cb0fd8d17234642e5a7/?ulp='
                    u'[[[http://www.boutique.ru/jewelleryandgifts/'
                    u'svechy_in_gifts/commedesgarcons/'
                    u'e9aeb173-a43a-11dd-892e-00304833051e]]]',
            u'vendor': {
                u'id': 1,
                u'name': u'Comme des Garcons'
            }
        }
    ]
}


class ProductVendorsTestCase(BaseTestCase):

    def test_get_product_vendors_request(self):
        self.set_mocker(ProductVendors.URL, limit=1)
        result = {
            u'_meta': {
                u'count': 752,
                u'limit': 1,
                u'offset': 0
            },
            u'results': [
                {
                    u'id': 1,
                    u'name': u'Comme des Garcons'
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.ProductVendors.get(limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.mocker.verify()

    def test_get_product_vendors_with_id_request(self):
        self.set_mocker(ProductVendors.SINGLE_URL, id=1, with_pagination=False)
        result = {
            u'id': 1,
            u'name': u'Comme des Garcons'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.ProductVendors.getOne(1)
        self.assertEqual(res[u'id'], 1)
        self.mocker.verify()


class ProductCategoriesTestCase(BaseTestCase):

    def test_get_product_categories_request(self):
        self.set_mocker(ProductCategories.URL, limit=4)
        result = {
            u'_meta': {
                u'count': 4,
                u'limit': 4,
                u'offset': 0
            },
            u'results': [
                {
                    u'id': 1,
                    u'name': u'category1'
                },
                {
                    u'id': 2,
                    u'name': u'category2'
                },
                {
                    u'id': 3,
                    u'name': u'category-child1',
                    u'parent': {
                        u'id': 1,
                        u'name': u'category1',
                        u'parent': None
                    }
                },
                {
                    u'id': 4,
                    u'name': u'category4'
                }
            ]
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.ProductCategories.get(limit=4)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 4)
        self.assertEqual(len(res[u'results']), 4)
        self.mocker.verify()

    def test_get_product_categories_with_id_request(self):
        self.set_mocker(
            ProductCategories.SINGLE_URL, id=1, with_pagination=False)
        result = {
            u'id': 1,
            u'name': u'category1'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.ProductCategories.getOne(1)
        self.assertEqual(res[u'id'], 1)
        self.mocker.verify()


class ProductCampaignsTestCase(BaseTestCase):

    def test_get_product_campaigns_request(self):
        self.set_mocker(ProductCampaigns.URL, id=25, limit=1)
        result = {
            u'results': [
                {
                    u'count': 189,
                    u'id': 6,
                    u'name': u'AdvCamp 1'
                }
            ],
            u'_meta': {
                u'count': 2,
                u'limit': 1,
                u'offset': 0
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.ProductCampaigns.get(25, limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.assertEqual(len(res[u'results']), 1)
        self.mocker.verify()

    def test_get_product_campaigns_with_id_request(self):
        self.set_mocker(
            ProductCampaigns.SINGLE_URL, id=25, c_id=6, with_pagination=False)
        result = {
            u'count': 189,
            u'id': 6,
            u'name': u'AdvCamp 1'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.ProductCampaigns.getOne(25, 6)
        self.assertEqual(res[u'id'], 6)
        self.mocker.verify()


class ProductsTestCase(BaseTestCase):

    def test_get_products_request(self):
        self.set_mocker(Products.URL, id=25, limit=1, offset=1)
        result = PRODUCTS_RESULT
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Products.get(25, limit=1, offset=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.assertEqual(len(res[u'results']), 1)
        self.mocker.verify()

    def test_get_products_with_id_request(self):
        self.set_mocker(
            Products.SINGLE_URL, id=25, p_id=2, with_pagination=False)
        result = PRODUCTS_RESULT['results'][0]
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Products.getOne(25, 2)
        self.assertEqual(res[u'id'], 2)
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
