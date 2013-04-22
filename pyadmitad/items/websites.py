from pyadmitad.items.base import Item


__all__ = (
    'Websites',
    'WebsitesManage'
)


class Websites(Item):
    """
    List of websites

    Required scope - "websites"
    """
    URL = Item.prepare_url('websites')
    SINGLE_URL = Item.prepare_url('websites/%(id)s')

    STATUS_FILTERING = ('new', 'pending', 'active', 'suspended', 'declined')
    CAMPAIGN_STATUS_FILTERING = ('pending', 'active', 'declined', 'disabled')
    FILTERING = {
        'status': lambda x: x if x in Websites.STATUS_FILTERING else None,
        'campaign_status': (
            lambda x: x if x in Websites.CAMPAIGN_STATUS_FILTERING else None),
    }

    def get(self, **kwargs):
        """
        res = client.Websites.get()
        res = client.Websites.get(status='new', campaign_status='active')

        """
        kwargs['url'] = self.URL
        kwargs['allowed_filtering'] = self.FILTERING
        return self.transport.GET.set_pagination(**kwargs).\
            set_filtering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        res = client.Websites.getOne(_id=2)
        res = client.Websites.getOne2(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.GET.request(**kwargs)


class WebsitesManage(Item):
    """
    Manage websites

    Required scope - "manage_websites"
    """
    CREATE_URL = Item.prepare_url('website/create')
    UPDATE_URL = Item.prepare_url('website/update/%(id)s')
    VERIFY_URL = Item.prepare_url('website/verify/%(id)s')
    DELETE_URL = Item.prepare_url('website/delete/%(id)s')

    FIELDS = {
        'name': lambda x: Item.sanitize_string_value(x, 'name', max_length=200),
        'kind': lambda x: Item.sanitize_string_value(x, 'kind', max_length=20),
        'language': lambda x: Item.sanitize_string_value(
            x, 'language', max_length=2),
        'adservice': lambda x: Item.sanitize_integer_value(
            x, 'adservice', blank=True),
        'site_url': lambda x: Item.sanitize_string_value(
            x, 'site_url', max_length=255),
        'description': lambda x: Item.sanitize_string_value(
            x, 'description', max_length=20000, min_length=100),
        'categories': lambda x: Item.sanitize_integer_array(x, 'categories'),
        'regions': lambda x: Item.sanitize_string_array(
            x, 'regions', max_length=2),
        'atnd_visits': lambda x: Item.sanitize_integer_value(
            x, 'atnd_visits', blank=False),
        'atnd_hits': lambda x: Item.sanitize_integer_value(
            x, 'atnd_hits', blank=False)
    }

    def sanitize_fields(self, **kwargs):
        for field in self.FIELDS:
            kwargs[field] = self.FIELDS[field](kwargs.get(field))
        return kwargs

    def create(self, **kwargs):
        """
        res = client.WebsitesManage.create(name='test', ....)

        """
        data = self.sanitize_fields(**kwargs)
        kwargs['url'] = self.CREATE_URL
        kwargs.pop('language', None)
        return self.transport.POST.set_data(data).request(**kwargs)
