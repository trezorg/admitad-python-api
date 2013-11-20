# -*- coding: utf-8 -*-

import unittest
from pyadmitad.tests.base import BaseTestCase
from pyadmitad.items.auxiliary import *


class WebsiteTypesTestCase(BaseTestCase):

    def test_get_website_types_request(self):
        self.set_mocker(WebsiteTypes.URL)
        result = {
            u'results': [
                u'website',
                u'doorway',
                u'contextual',
                u'social_app',
                u'social_group',
                u'social_teaser',
                u'arbitrage'
            ],
            u'_meta': {
                u'count': 7,
                u'limit': 20,
                u'offset': 0
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.WebsiteTypes.get()
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.mocker.verify()

    def test_get_website_types_request_with_pagination(self):
        self.set_mocker(WebsiteTypes.URL, offset=1, limit=2)
        result = {
            u'results': [
                u'doorway',
                u'contextual'
            ],
            u'_meta': {
                u'count': 7,
                u'limit': 2,
                u'offset': 1
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.WebsiteTypes.get(offset=1, limit=2)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertEqual(len(res[u'results']), 2)
        _meta = res[u'_meta']
        self.assertEqual(_meta[u'count'], 7)
        self.assertEqual(_meta[u'limit'], 2)
        self.assertEqual(_meta[u'offset'], 1)
        self.mocker.verify()


class WebsiteRegionsTestCase(BaseTestCase):

    def test_get_website_regions_request(self):
        self.set_mocker(WebsiteRegions.URL)
        result = {
            u'results': [
                u'RU', u'UA', u'BY', u'KZ', u'DE', u'FR', u'US', u'AM', u'AU',
                u'AZ', u'CA', u'EE', u'GE', u'KG', u'LV', u'LT', u'MD', u'TJ',
                u'TM', u'UZ'
            ],
            u'_meta': {
                u'count': 20,
                u'limit': 20,
                u'offset': 0
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.WebsiteRegions.get()
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()

    def test_get_website_regions_request_with_pagination(self):
        self.set_mocker(WebsiteRegions.URL, offset=1, limit=2)
        result = {
            u'results': [u'UA', u'BY'],
            u'_meta': {
                u'count': 20,
                u'limit': 2,
                u'offset': 1
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.WebsiteRegions.get(offset=1, limit=2)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(len(res[u'results']), 2)
        _meta = res[u'_meta']
        self.assertEqual(_meta[u'count'], 20)
        self.assertEqual(_meta[u'limit'], 2)
        self.assertEqual(_meta[u'offset'], 1)
        self.mocker.verify()


class SystemLanguagesTestCase(BaseTestCase):

    def test_get_languages_request(self):
        self.set_mocker(SystemLanguages.URL)
        result = {
            u'results': [
                {
                    u'flag': u'https://admitad.com/media/images/flags/'
                             u'c8ef33a926799c7c3d7103212a78b187.png',
                    u'language': u'Русский',
                    u'language_code': u'ru'
                },
                {
                    u'flag': u'',
                    u'language': u'Deutsch',
                    u'language_code': u'de'
                }
            ],
            u'_meta': {
                u'count': 2,
                u'limit': 20,
                u'offset': 0
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.SystemLanguages.get()
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()

    def test_get_language_request_with_code(self):
        self.set_mocker(SystemLanguages.SINGLE_URL,
                        code='ru', with_pagination=False)
        result = {
            u'flag': u'https://admitad.trezor.by/media/images/flags/'
                     u'c8ef33a926799c7c3d7103212a78b187.png',
            u'language': u'Русский',
            u'language_code': u'ru'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.SystemLanguages.getOne(code='ru')
        self.assertIn(u'flag', res)
        self.assertIn(u'language', res)
        self.assertIn(u'language_code', res)
        self.mocker.verify()


class SystemCurrenciesTestCase(BaseTestCase):

    def test_get_currencies_request(self):
        self.set_mocker(SystemCurrencies.URL)
        result = {
            u'results': [
                {
                    u'code': u'EUR',
                    u'min_sum': u'20.00',
                    u'name': u'Евро',
                    u'sign': u'€'
                },
                {
                    u'code': u'RUB',
                    u'min_sum': u'750.00',
                    u'name': u'Российский рубль',
                    u'sign': u'руб.'
                },
                {
                    u'code': u'USD',
                    u'min_sum': u'25.00',
                    u'name': u'Американский доллар',
                    u'sign': u'$'
                }
            ],
            u'_meta': {
                u'count': 3,
                u'limit': 20,
                u'offset': 0
            },
            }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.SystemCurrencies.get()
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()

    def test_get_currencies_request_with_pagination(self):
        self.set_mocker(SystemCurrencies.URL, offset=1, limit=1)
        result = {
            u'results': [
                {
                    u'code': u'RUB',
                    u'min_sum': u'750.00',
                    u'name': u'Российский рубль',
                    u'sign': u'руб.'
                }
            ],
            u'_meta': {
                u'count': 3,
                u'limit': 1,
                u'offset': 1
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.SystemCurrencies.get(offset=1, limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.assertEqual(res[u'_meta'][u'offset'], 1)
        self.mocker.verify()


class AdvertiserServiceTestCase(BaseTestCase):

    def test_get_advertiser_services(self):
        self.set_mocker(AdvertiserServices.URL)
        result = {
            u'results': [
                {
                    u'allowed_referrers': u'',
                    u'id': 1,
                    u'logo': u'https://admitad.com/media/adservice/images/'
                             u'755c6ece4a7f2a45548737c212906434.png',
                    u'name': u'Yandex.Direct',
                    u'url': u'http://direct.yandex.ru/'
                },
                {
                    u'allowed_referrers': u'',
                    u'id': 2,
                    u'logo': u'https://admitad.com/media/adservice/images/'
                             u'273ad9483718164ffd05066a8bebec46.png',
                    u'name': u'Бегун',
                    u'url': u'http://begun.ru/'
                }
            ],
            u'_meta': {
                u'count': 2,
                u'limit': 20,
                u'offset': 0
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.AdvertiserServices.get()
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()

    def test_get_advertiser_services_with_pagination(self):
        self.set_mocker(AdvertiserServices.URL, offset=1, limit=1)
        result = {
            u'results': [
                {
                    u'allowed_referrers': u'',
                    u'id': 2,
                    u'logo': u'https://admitad.com/media/adservice/images/'
                             u'273ad9483718164ffd05066a8bebec46.png',
                    u'name': u'Бегун',
                    u'url': u'http://begun.ru/'
                }
            ],
            u'_meta': {
                u'count': 2,
                u'limit': 1,
                u'offset': 1
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.AdvertiserServices.get(offset=1, limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.assertEqual(res[u'_meta'][u'offset'], 1)
        self.mocker.verify()

    def test_get_advertiser_services_with_id(self):
        self.set_mocker(
            AdvertiserServices.SINGLE_URL,
            **{'id': 2, 'with_pagination': False})
        result = {
            u'allowed_referrers': u'',
            u'id': 2,
            u'logo': u'https://admitad.com/media/adservice/images/'
                     u'273ad9483718164ffd05066a8bebec46.png',
            u'name': u'Бегун',
            u'url': u'http://begun.ru/'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.AdvertiserServices.getOne(_id=2)
        self.assertEqual(res[u'id'], 2)
        self.mocker.verify()

    def test_get_advertiser_services_with_kind(self):
        self.set_mocker(AdvertiserServices.KIND_URL, kind='contextual')
        result = {
            u'results': [
                {
                    u'allowed_referrers': u'',
                    u'id': 1,
                    u'logo': u'https://admitad.com/media/adservice/images/'
                             u'755c6ece4a7f2a45548737c212906434.png',
                    u'name': u'Yandex.Direct',
                    u'url': u'http://direct.yandex.ru/'
                },
                {
                    u'allowed_referrers': u'',
                    u'id': 2,
                    u'logo': u'https://admitad.com/media/adservice/images/'
                             u'273ad9483718164ffd05066a8bebec46.png',
                    u'name': u'Бегун',
                    u'url': u'http://begun.ru/'
                }
            ],
            u'_meta': {
                u'count': 2,
                u'limit': 20,
                u'offset': 0
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.AdvertiserServices.getForKind(kind='contextual')
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()

    def test_get_advertiser_services_with_kind_and_id(self):
        self.set_mocker(AdvertiserServices.KIND_SINGLE_URL,
                        id=2, kind='contextual', with_pagination=False)
        result = {
            u'allowed_referrers': u'',
            u'id': 2,
            u'logo': u'https://admitad.com/media/adservice/images/'
                     u'273ad9483718164ffd05066a8bebec46.png',
            u'name': u'Бегун',
            u'url': u'http://begun.ru/'
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.AdvertiserServices.getForKindOne(2, 'contextual')
        self.assertEqual(res[u'id'], 2)
        self.mocker.verify()


class CampaignsCategoriesTestCase(BaseTestCase):

    def test_get_campaigns_categories(self):
        self.set_mocker(CampaignCategories.URL)
        result = {
            u'results': [
                {
                    u'id': 3,
                    u'name': u'Браузерные',
                    u'parent': {
                        u'id': 2,
                        u'name': u'Онлайн-игр',
                        u'parent': None
                    }
                },
                {
                    u'id': 5,
                    u'name': u'Другая',
                    u'parent': None
                },
                {
                    u'id': 4,
                    u'name': u'Клиентские',
                    u'parent': {
                        u'id': 2,
                        u'name': u'Онлайн-игры',
                        u'parent': None
                    }
                }
            ],
            u'_meta': {
                u'count': 3,
                u'limit': 20,
                u'offset': 0
            }
        }

        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.CampaignCategories.get()
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.mocker.verify()

    def test_get_campaigns_categories_with_pagination(self):
        self.set_mocker(CampaignCategories.URL, limit=3)
        result = {
            u'results': [
                {
                    u'id': 3,
                    u'name': u'Браузерные',
                    u'parent': {
                        u'id': 2,
                        u'name': u'Онлайн-игр',
                        u'parent': None
                    }
                },
                {
                    u'id': 5,
                    u'name': u'Другая',
                    u'parent': None
                },
                {
                    u'id': 4,
                    u'name': u'Клиентские',
                    u'parent': {
                        u'id': 2,
                        u'name': u'Онлайн-игры',
                        u'parent': None
                    }
                }
            ],
            u'_meta': {
                u'count': 3,
                u'limit': 3,
                u'offset': 0
            }
        }

        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.CampaignCategories.get(limit=3)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 3)
        self.mocker.verify()

    def test_get_campaigns_categories_with_id(self):
        self.set_mocker(
            CampaignCategories.SINGLE_URL, id=3, with_pagination=False)
        result = {
            u'id': 3,
            u'name': u'Браузерные',
            u'parent': {
                u'id': 2,
                u'name': u'Онлайн-игр',
                u'parent': None
            }
        }
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.CampaignCategories.getOne(3)
        self.assertEqual(res[u'id'], 3)
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
