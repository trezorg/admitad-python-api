# coding: utf-8

from pyadmitad.items.base import Item


__all__ = [
    'LostOrders',
    'LostOrdersManager',
]


class LostOrders(Item):

    SCOPE = 'lost_orders'

    URL = Item.prepare_url('lost_orders')
    SINGLE_URL = Item.prepare_url('lost_orders/%(lost_order_id)s')

    def get(self, **kwargs):
        kwargs['url'] = self.URL
        return self.transport.get().set_pagination().request(**kwargs)

    def getOne(self, lost_order_id, **kwargs):
        kwargs['url'] = self.SINGLE_URL
        kwargs['lost_order_id'] = self.sanitize_id(lost_order_id)
        return self.transport.get().request(**kwargs)


class LostOrdersManager(Item):

    SCOPE = 'manage_lost_orders'

    DELETE_URL = Item.prepare_url('lost_orders/%(lost_order_id)s/decline')
    CREATE_URL = Item.prepare_url('lost_orders/create')

    CREATE_FIELDS = {
        'advcampaign': lambda x: Item.sanitize_integer_value(x, 'advcampaign'),
        'website': lambda x: Item.sanitize_integer_value(x, 'website'),
        'order_id': lambda x: Item.sanitize_string_value(x, 'order_id'),
        'order_date': lambda x: Item.sanitize_string_value(x, 'order_date'),
        'order_price': lambda x: Item.sanitize_float_value(x, 'order_price'),
        'comment': lambda x: Item.sanitize_string_value(x, 'comment'),
    }

    def delete(self, lost_order_id):
        data = {
            'url': self.DELETE_URL,
            'lost_order_id': self.sanitize_id(lost_order_id),
        }
        return self.transport.set_method('DELETE').request(**data)

    def create(self, attachment, **kwargs):
        data = self.sanitize_fields(self.CREATE_FIELDS, **kwargs)
        kwargs['url'] = self.CREATE_URL
        files = {
            'attachment': attachment,
        }
        return self.transport.post().set_data(data).set_files(files).request(**kwargs)
