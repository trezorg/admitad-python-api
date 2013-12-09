from copy import deepcopy
from pyadmitad.items.base import Item


__all__ = (
    'MoneyTransfers',
    'MoneyTransfersManage',
)


class MoneyTransfersBase(Item):

    ORDERING = ('date_created',)
    FILTERING = {
        'sender': Item.to_unicode,
        'recipient': Item.to_unicode,
        'currency': Item.to_unicode,
    }


class MoneyTransfers(Item):
    """
    List of webmaster money transfers

    Required scope - "webmaster_money_transfers"
    """
    URL = Item.prepare_url('webmaster_money_transfers')
    SINGLE_URL = Item.prepare_url('webmaster_money_transfer/%(id)s')

    def get(self, **kwargs):
        """
        res = client.MoneyTransfers.get()
        res = client.MoneyTransfers.get(limit=2)

        """
        kwargs['url'] = self.URL
        return self.transport.set_method('GET').\
            set_pagination(**kwargs).set_filtering(**kwargs).\
            set_ordering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        res = client.MoneyTransfers.getOne(_id=2)
        res = client.MoneyTransfers.getOne(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('GET').request(**kwargs)


class MoneyTransfersManage(Item):
    """
    Manage webmaster money transfers

    Required scope - "manage_webmaster_money_transfers"
    """
    CREATE_FIELDS = {
        'comment': lambda x: Item.sanitize_string_value(x, 'comment'),
        'recipient': lambda x: Item.sanitize_string_value(x, 'recipient'),
        'currency': lambda x: Item.sanitize_currency(x, 'currency'),
        'sum': lambda x: Item.sanitize_float_value(x, 'sum')
    }

    CREATE_URL = Item.prepare_url('webmaster_money_transfer/create')

    @staticmethod
    def sanitize_fields(fields, **kwargs):
        data = deepcopy(kwargs)
        for field in fields:
            data[field] = fields[field](data.get(field))
        return dict([(key, value) for (key, value) in data.items() if value])

    def create(self, **kwargs):
        """
        Create a webmaster money transfers

        res = client.MoneyTransfersManage.create(
            sender='webmaster',
            recipient='recipient',
            sum=200,
            currency='USD',
            comment='comment')

        """
        data = self.sanitize_fields(self.CREATE_FIELDS, **kwargs)
        kwargs['url'] = self.CREATE_URL
        return self.transport.set_method('POST').\
            set_data(data).request(**kwargs)
