from pyadmitad.items.base import Item


class LinksValidator(Item):

    URL = Item.prepare_url('validate_links')

    GET_FIELDS = {
        'link': lambda x: Item.sanitize_string_value(x, 'link'),
    }

    def get(self, link, **kwargs):
        data = self.sanitize_fields(self.GET_FIELDS, link=link)
        kwargs['url'] = self.URL
        return self.transport.get().set_data(data).request(**kwargs)
