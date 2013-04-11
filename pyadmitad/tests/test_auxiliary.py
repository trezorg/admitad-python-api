# -*- coding: utf-8 -*-

import unittest
from mocker import MockerTestCase
from pyadmitad.api import get_oauth_client
from pyadmitad.constants import *
from pyadmitad.transport import prepare_api_url, build_headers, \
    HttpTransportPagination


class AuxiliaryBase(MockerTestCase):
    def set_mocker(self, url, **kwargs):
        access_token = 'access_token'
        with_pagination = kwargs.pop('with_pagination', True)
        self.client = get_oauth_client(access_token)
        obj = self.mocker.patch(self.client.transport)
        url = prepare_api_url(url, **kwargs)
        kwargs = {
            'data': with_pagination and
            HttpTransportPagination(**kwargs).to_value() or None,
            'headers': build_headers(access_token),
            'method': 'GET'
        }
        obj.api_request(url, **kwargs)


class WebsiteTypesTestCase(AuxiliaryBase):
    def test_get_website_types_request(self):
        self.set_mocker(WEBSITE_TYPES_URL)
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
        self.set_mocker(WEBSITE_TYPES_URL, offset=1, limit=2)
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


class WebsiteRegionsTestCase(AuxiliaryBase):
    def test_get_website_regions_request(self):
        self.set_mocker(WEBSITE_REGIONS_URL)
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
        self.set_mocker(WEBSITE_REGIONS_URL, offset=1, limit=2)
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


class SystemLanguagesTestCase(AuxiliaryBase):
    def test_get_languages_request(self):
        self.set_mocker(LANGUAGES_URL)
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

    def test_get_language_request(self):
        self.set_mocker(LANGUAGES_SINGLE_URL, code='ru', with_pagination=False)
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


if __name__ == '__main__':
    unittest.main()
