# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import Campaigns, CampaignsForWebsite,\
    CampaignsManage
from pyadmitad.tests.base import BaseTestCase


CAMPAIGNS_RESULT = {
    "results": [
        {
            "status": "active",
            "rating": "5.00",
            "description": "Gmail is a mail service by google",
            "actions": [
                {
                    "payment_size": "50.00",
                    "hold_time": 120,
                    "percentage": True,
                    "name": "action name",
                    "id": 1
                },
                {
                    "payment_size": "12.00",
                    "hold_time": 30,
                    "percentage": True,
                    "name": "Покупка",
                    "id": 15
                },
                {
                    "payment_size": "11.00",
                    "hold_time": 15,
                    "percentage": False,
                    "name": "Регистрация",
                    "id": 11
                }
            ],
            "site_url": "http://www.gmail.com/",
            "regions": [
                {
                    "region": "01"
                },
                {
                    "region": "BY"
                },
                {
                    "region": "CA"
                },
                {
                    "region": "DE"
                },
                {
                    "region": "KZ"
                },
                {
                    "region": "RU"
                },
                {
                    "region": "US"
                }
            ],
            "currency": "USD",
            "cr": None,
            "ecpc": None,
            "id": 6,
            "categories": [
                {
                    "name": "Магазин",
                    "parent": None,
                    "id": 1
                },
                {
                    "name": "Онлайн-игры",
                    "parent": None,
                    "id": 2
                },
                {
                    "name": "Браузерные",
                    "parent": {
                        "name": "Онлайн-игры",
                        "parent": None,
                        "id": 2
                    },
                    "id": 3
                }
            ],
            "name": "Campaign2"
        }
    ],
    "_meta": {
        "count": 4,
        "limit": 1,
        "offset": 0
    }
}

CAMPAIGNS_FOR_WEBSITE_RESULT = {
    "results": [
        {
            "status": "active",
            "rating": "5.00",
            "traffics": [
                {
                    "enabled": False,
                    "name": "Тип 1",
                    "id": 1
                },
                {
                    "enabled": False,
                    "name": "Тип 2",
                    "id": 2
                }
            ],
            "ecpc": None,
            "description": "Gmail is a mail service by google",
            "name": "AdvCamp 1",
            "gotolink": "http://ad.admitad.com/goto/some_link/",
            "avg_hold_time": None,
            "actions": [
                {
                    "payment_size": "50.00",
                    "hold_time": 120,
                    "percentage": None,
                    "name": "action name",
                    "id": 1
                },
                {
                    "payment_size": "12.00",
                    "hold_time": 30,
                    "percentage": True,
                    "name": "Покупка",
                    "id": 15
                },
                {
                    "payment_size": "11.00",
                    "hold_time": 15,
                    "percentage": True,
                    "name": "Регистрация",
                    "id": 11
                }
            ],
            "site_url": "http://www.gmail.com/",
            "regions": [
                {
                    "region": "01"
                },
                {
                    "region": "BY"
                },
                {
                    "region": "CA"
                },
                {
                    "region": "DE"
                },
                {
                    "region": "KZ"
                },
                {
                    "region": "RU"
                },
                {
                    "region": "US"
                }
            ],
            "currency": "USD",
            "goto_cookie_lifetime": 45,
            "geotargeting": True,
            "cr": None,
            "activation_date": "2010-03-31 19:05:39",
            "max_hold_time": 120,
            "id": 6,
            "categories": [
                {
                    "name": "Магазин",
                    "parent": None,
                    "id": 1
                },
                {
                    "name": "Онлайн-игры",
                    "parent": None,
                    "id": 2
                },
                {
                    "name": "Браузерные",
                    "parent": {
                        "name": "Онлайн-игры",
                        "parent": None,
                        "id": 2
                    },
                    "id": 3
                },
                {
                    "name": "Другая",
                    "parent": None,
                    "id": 5
                },
                {
                    "name": "Финансы",
                    "parent": {
                        "name": "Другая",
                        "parent": None,
                        "id": 5
                    },
                    "id": 6
                },
                {
                    "name": "Подкатегория",
                    "parent": {
                        "name": "Другая",
                        "parent": None,
                        "id": 5
                    },
                    "id": 17
                }
            ],
            "percentage_of_confirmed": None
        }
    ],
    "_meta": {
        "count": 4,
        "limit": 1,
        "offset": 0
    }
}

CAMPAIGN_CONNECT_RESULT = {
    "message": "Заявка на добавление кампании Campaign успешно создана.",
    "success": "OK"
}

CAMPAIGN_DISCONNECT_RESULT = {
    "message": "Кампания Campaign была удалена из ваших предложений."
               " Вы можете позже добавить ее снова.",
    "success": "Deleted"
}


class CampaignsTestCase(BaseTestCase):

    def test_get_campaigns_request(self):
        self.set_mocker(Campaigns.URL, limit=1)
        self.mocker.result(CAMPAIGNS_RESULT)
        self.mocker.replay()
        res = self.client.Campaigns.get(limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.mocker.verify()

    def test_get_campaigns_request_with_id(self):
        self.set_mocker(Campaigns.SINGLE_URL, id=6, with_pagination=False)
        self.mocker.result(CAMPAIGNS_RESULT['results'][0])
        self.mocker.replay()
        res = self.client.Campaigns.getOne(6)
        self.assertEqual(res[u'id'], 6)
        self.mocker.verify()


class CampaignsForWebsiteTestCase(BaseTestCase):

    def test_get_campaigns_for_websites_request(self):
        self.set_mocker(CampaignsForWebsite.URL, id=22, limit=1)
        self.mocker.result(CAMPAIGNS_FOR_WEBSITE_RESULT)
        self.mocker.replay()
        res = self.client.CampaignsForWebsite.get(22, limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.mocker.verify()

    def test_get_campaigns_request_with_id(self):
        self.set_mocker(
            CampaignsForWebsite.SINGLE_URL, id=22,
            c_id=6, with_pagination=False)
        self.mocker.result(CAMPAIGNS_FOR_WEBSITE_RESULT['results'][0])
        self.mocker.replay()
        res = self.client.CampaignsForWebsite.getOne(22, 6)
        self.assertEqual(res[u'id'], 6)
        self.mocker.verify()


class CampaignsConnectWebsiteTestCase(BaseTestCase):

    def test_campaign_connect_websites_request(self):
        self.set_mocker(CampaignsManage.CONNECT_URL, w_id=22,
                        c_id=6, with_pagination=False, method='POST')
        self.mocker.result(CAMPAIGN_CONNECT_RESULT)
        self.mocker.replay()
        res = self.client.CampaignsManage.connect(c_id=6, w_id=22)
        self.assertIn(u'message', res)
        self.assertIn(u'success', res)
        self.mocker.verify()

    def test_campaign_disconnect_websites_request(self):
        self.set_mocker(CampaignsManage.DISCONNECT_URL, w_id=22,
                        c_id=6, with_pagination=False, method='POST')
        self.mocker.result(CAMPAIGN_CONNECT_RESULT)
        self.mocker.replay()
        res = self.client.CampaignsManage.disconnect(c_id=6, w_id=22)
        self.assertIn(u'message', res)
        self.assertIn(u'success', res)
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
