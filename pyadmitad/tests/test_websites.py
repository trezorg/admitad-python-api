# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import Websites, WebsitesManage
from pyadmitad.tests.base import BaseTestCase


WEBSITE_CREATE_DATA = dict(
    regions=['RU'],
    atnd_hits='20',
    atnd_visits='10',
    name='website1',
    language='ru',
    site_url='http://google.com',
    description='descriptiondescriptiondescriptiondescription'
                'descriptiondescriptiondescriptiondescription'
                'descriptiondescription',
    categories=['1', '2'],
    kind='website'
)


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
                    u'language': 'ru',
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
            u'language': 'ru',
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


class WebsitesManageTestCase(BaseTestCase):

    def test_create_website_request(self):
        self.set_mocker(
            WebsitesManage.CREATE_URL,
            method='POST',
            with_pagination=False,
            data=WEBSITE_CREATE_DATA)
        result = {
            u'atnd_hits': 20,
            u'atnd_visits': 10,
            u'categories': [
                {
                    u'id': 1,
                    u'name': u'Магазин',
                    u'parent': None
                },
                {
                    u'id': 2,
                    u'name': u'Онлайн-игры',
                    u'parent': None
                }
            ],
            u'creation_date': u'2013-04-22 14:41:29',
            u'description': u'descriptiondescriptiondescriptiondescription'
                            u'descriptiondescriptiondescriptiondescription'
                            u'descriptiondescription',
            u'id': 52,
            u'is_old': False,
            u'kind': u'website',
            u'language': u'ru',
            u'name': u'website1',
            u'regions': [
                {
                    u'id': 25,
                    u'region': u'RU'
                }
            ],
            u'site_url': u'http://google.com/',
            u'status': u'new',
            u'verification_code': u'fde88f4b6b'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.WebsitesManage.create(**WEBSITE_CREATE_DATA)
        self.assertIn(u'id', res)
        self.assertEqual(u'new', res['status'])
        self.assertEqual(u'website', res['kind'])
        self.mocker.verify()

    def test_update_website_request(self):
        self.set_mocker(
            WebsitesManage.UPDATE_URL,
            id=52,
            method='POST',
            with_pagination=False,
            data={'language': 'de', 'name': 'test-update'})
        result = {
            u'atnd_hits': 20,
            u'atnd_visits': 10,
            u'categories': [
                {
                    u'id': 1,
                    u'name': u'Магазин',
                    u'parent': None
                },
                {
                    u'id': 2,
                    u'name': u'Онлайн-игры',
                    u'parent': None
                }
            ],
            u'creation_date': u'2013-04-22 14:41:29',
            u'description': u'descriptiondescriptiondescriptiondescription'
                            u'descriptiondescriptiondescriptiondescription'
                            u'descriptiondescription',
            u'id': 52,
            u'is_old': False,
            u'kind': u'website',
            u'language': u'de',
            u'name': u'test-update',
            u'regions': [
                {
                    u'id': 25,
                    u'region': u'RU'
                }
            ],
            u'site_url': u'http://google.com/',
            u'status': u'new',
            u'verification_code': u'fde88f4b6b'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.WebsitesManage.update(
            52, language='de', name='test-update')
        self.assertIn(u'id', res)
        self.assertEqual(u'test-update', res['name'])
        self.assertEqual(u'de', res['language'])
        self.mocker.verify()

    def test_verify_website_request(self):
        self.set_mocker(
            WebsitesManage.VERIFY_URL,
            id=52, method='POST', with_pagination=False)
        result = {
            "message": "Площадка прошла автоматическую проверку."
                       " Ожидайте подтверждения администрацией.",
            "success": "Accepted"
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.WebsitesManage.verify(52)
        self.assertIn(u'success', res)

    def test_delete_website_request(self):
        self.set_mocker(
            WebsitesManage.DELETE_URL,
            id=52, method='POST', with_pagination=False)
        result = {
            "message": "Площадка удалена успешно.",
            "success": "Deleted"
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.WebsitesManage.delete(52)
        self.assertIn(u'success', res)


if __name__ == '__main__':
    unittest.main()
