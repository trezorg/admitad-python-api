# -*- coding: utf-8 -*-

from mocker import MockerTestCase
from pyadmitad.api import get_oauth_client
from pyadmitad.transport import build_headers, \
    HttpTransportPagination, HttpTransportOrdering, HttpTransportFiltering


class BaseTestCase(MockerTestCase):

    def prepare_data(self, **kwargs):
        with_pagination = kwargs.pop('with_pagination', True)
        with_ordering = kwargs.pop('with_ordering', True)
        with_filtering = kwargs.pop('with_filtering', True)
        data = kwargs.get('data', {}) or {}
        if with_pagination:
            data.update(HttpTransportPagination(**kwargs).to_value())
        if with_ordering:
            data.update(HttpTransportOrdering(**kwargs).to_value())
        if with_filtering:
            data.update(HttpTransportFiltering(**kwargs).to_value())
        return data or None

    @staticmethod
    def prepare_method(**kwargs):
        method = kwargs.get('method', 'GET')
        return method if method in ('POST', 'GET') else 'GET'

    def set_mocker(self, url, **kwargs):
        access_token = 'access_token'
        self.client = get_oauth_client(access_token)
        obj = self.mocker.patch(self.client.transport)
        url = url % kwargs
        kwargs = {
            'data': self.prepare_data(**kwargs),
            'headers': build_headers(access_token),
            'method': BaseTestCase.prepare_method(**kwargs),
            'debug': False
        }
        obj.api_request(url, **kwargs)
