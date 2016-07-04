from pyadmitad.items.base import Item


__all__ = [
    'DeeplinksManage',
]


class DeeplinksManage(Item):

    CREATE_URL = Item.prepare_url('deeplink/%(website_id)s/advcampaign/%(campaign_id)s')

    CREATE_FIELDS = {
        'ulp': lambda x: Item.sanitize_string_value(x, 'ulp'),
        'subid': lambda x: Item.sanitize_string_value(x, 'subid', max_length=30, blank=True),
        # todo: subid[1-4]
    }

    def create(self, website_id, campaign_id, **kwargs):
        data = self.sanitize_fields(self.CREATE_FIELDS, **kwargs)
        kwargs['url'] = self.CREATE_URL
        kwargs['website_id'] = self.sanitize_id(website_id)
        kwargs['campaign_id'] = self.sanitize_id(campaign_id)
        return self.transport.get().set_data(data).request(**kwargs)
