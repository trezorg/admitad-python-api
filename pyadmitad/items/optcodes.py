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

    def delete(self, optcode_id):
        data = {
            'url': self.DELETE_URL,
            'optcode_id': self.sanitize_id(optcode_id),
        }
        return self.transport.set_method('POST').request(**data)


class CampaignStatusOptCodesManager(BaseOptCodesManager):

    CREATE_URL = Item.prepare_url('opt_codes/offer/create')
    UPDATE_URL = Item.prepare_url('opt_codes/offer/update/%(optcode_id)s')


class ActionOptCodesManager(BaseOptCodesManager):

    CREATE_URL = Item.prepare_url('opt_codes/action/create')
    UPDATE_URL = Item.prepare_url('opt_codes/action/update/%(optcode_id)s')
