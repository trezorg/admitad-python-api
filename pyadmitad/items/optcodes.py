from pyadmitad.items.base import Item


__all__ = [
    'OptCodes',
    'CampaignStatusOptCodesManager',
    'ActionOptCodesManager',
]


class BaseOptCodes(Item):

    DESC_MODE_SIMPLE = 0
    DESC_MODE_EXTENDED = 1

    METHOD_GET = 0
    METHOD_POST = 1

    ACTION_TYPE_ALL = 0
    ACTION_TYPE_SALE = 1
    ACTION_TYPE_LEAD = 2

    ACTION_STATUS_NEW = 0
    ACTION_STATUS_APPROVED = 1
    ACTION_STATUS_DECLINED = 2
    ACTION_STATUS_PENDING = 3


class OptCodes(BaseOptCodes):

    URL = Item.prepare_url('opt_codes')
    SINGLE_URL = Item.prepare_url('opt_codes/%(optcode_id)s')

    def get(self, **kwargs):
        kwargs['url'] = self.URL
        return self.transport.get().set_pagination().request(**kwargs)

    def getOne(self, optcode_id, **kwargs):
        kwargs['url'] = self.SINGLE_URL
        kwargs['optcode_id'] = self.sanitize_id(optcode_id)
        return self.transport.get().request(**kwargs)


class BaseOptCodesManager(BaseOptCodes):

    DELETE_URL = Item.prepare_url('opt_codes/delete/%(optcode_id)s')
    CREATE_URL = ''
    UPDATE_URL = ''

    CREATE_FIELDS = {}
    UPDATE_FIELDS = {}

    def delete(self, optcode_id):
        data = {
            'url': self.DELETE_URL,
            'optcode_id': self.sanitize_id(optcode_id),
        }
        return self.transport.set_method('POST').request(**data)

    def create(self, **kwargs):
        data = self.sanitize_fields(self.CREATE_FIELDS, **kwargs)
        kwargs['url'] = self.CREATE_URL
        return self.transport.set_method('POST').set_data(data).request(**kwargs)

    def update(self, optcode_id, **kwargs):
        data = self.sanitize_fields(self.UPDATE_FIELDS, **kwargs)
        kwargs['url'] = self.UPDATE_URL
        kwargs['optcode_id'] = self.sanitize_id(optcode_id)
        return self.transport.set_method('POST').set_data(data).request(**kwargs)


class CampaignStatusOptCodesManager(BaseOptCodesManager):

    CREATE_URL = Item.prepare_url('opt_codes/offer/create')
    UPDATE_URL = Item.prepare_url('opt_codes/offer/update/%(optcode_id)s')

    CREATE_FIELDS = {
    }
    UPDATE_FIELDS = {
    }


class ActionOptCodesManager(BaseOptCodesManager):

    CREATE_URL = Item.prepare_url('opt_codes/action/create')
    UPDATE_URL = Item.prepare_url('opt_codes/action/update/%(optcode_id)s')

    CREATE_FIELDS = {
        'website': lambda x: Item.sanitize_integer_value(x, 'website', blank=True),
        'campaign': lambda x: Item.sanitize_integer_value(x, 'campaign', blank=True),
        'desc_mode': lambda x: Item.sanitize_integer_value(x, 'desc_mode'),
        'url': lambda x: Item.sanitize_string_value(x, 'url'),
        'method': lambda x: Item.sanitize_integer_value(x, 'method'),
        'action_type': lambda x: Item.sanitize_integer_value(x, 'action_type'),
        'status': lambda x: Item.sanitize_integer_value(x, 'status'),
    }
    UPDATE_FIELDS = {
        'desc_mode': lambda x: Item.sanitize_integer_value(x, 'desc_mode', blank=True),
        'url': lambda x: Item.sanitize_string_value(x, 'url', blank=True),
        'method': lambda x: Item.sanitize_integer_value(x, 'method', blank=True),
        'action_type': lambda x: Item.sanitize_integer_value(x, 'action_type', blank=True),
        'status': lambda x: Item.sanitize_integer_value(x, 'status', blank=True),
    }
