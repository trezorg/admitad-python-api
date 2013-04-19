# -*- coding: utf-8 -*-

import unittest
from pyadmitad.items import Announcements, AnnouncementsManage
from pyadmitad.tests.base import BaseTestCase


ANNOUNCEMENTS_RESULTS = {
    u'results': [
        {
            u'message': u'Сотрудничество подтверждено',
            u'id': 264,
            u'advcampaign': {
                u'id': 8,
                u'name': u'AdvCamp 3'
            },
            u'event': u'request_accepted'
        }
    ],
    u'_meta': {
        u'count': 50,
        u'limit': 1,
        u'offset': 0
    }
}

ANNOUNCEMENTS_DELETE_RESULTS = {
    u'message': u'Оповещение удалено успешно.',
    u'success': u'Deleted'
}


class AnnouncementsTestCase(BaseTestCase):

    def test_get_announcements_request(self):
        self.set_mocker(Announcements.URL, limit=1)
        result = ANNOUNCEMENTS_RESULTS
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Announcements.get(limit=1)
        self.assertIn(u'results', res)
        self.assertIn(u'_meta', res)
        self.assertIsInstance(res[u'results'], list)
        self.assertIsInstance(res[u'_meta'], dict)
        self.assertEqual(res[u'_meta'][u'limit'], 1)
        self.mocker.verify()

    def test_get_announcements_request_with_id(self):
        self.set_mocker(Announcements.SINGLE_URL, id=264, with_pagination=False)
        result = ANNOUNCEMENTS_RESULTS['results'][0]
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.Announcements.getOne(264)
        self.assertEqual(res[u'id'], 264)
        self.mocker.verify()


class AnnouncementsManageTestCase(BaseTestCase):

    def test_delete_announcements_request(self):
        self.set_mocker(
            AnnouncementsManage.DELETE_URL, id=264,
            with_pagination=False, method='POST')
        result = ANNOUNCEMENTS_DELETE_RESULTS
        self.mocker.result(result)
        self.mocker.replay()
        res = self.client.AnnouncementsManage.delete(264)
        self.assertIn(u'message', res)
        self.assertIn(u'success', res)
        self.mocker.verify()


if __name__ == '__main__':
    unittest.main()
