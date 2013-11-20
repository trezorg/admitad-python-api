from pyadmitad.items.base import Item

__all__ = (
    'ProductCategories',
    'ProductVendors',
    'ProductCampaigns',
    'Products',
)


class ProductCategories(Item):
    """
    List of products categories

    Required scope - "public_data"
    """
    URL = Item.prepare_url('products/categories')
    SINGLE_URL = Item.prepare_url('products/categories/%(id)s')

    ORDERING = ('name',)

    def get(self, **kwargs):
        """
        res = client.ProductCategories.get()
        res = client.ProductCategories.get(limit=1, order_by=-name)
        """
        kwargs['url'] = self.URL
        kwargs['allowed_ordering'] = self.ORDERING
        return self.transport.set_method('GET').set_pagination(**kwargs).\
            set_ordering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        Here _id is category id.

        res = client.ProductCategories.getOne(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('GET').request(**kwargs)


class ProductVendors(Item):
    """
    List of products vendors

    Required scope - "public_data"
    """
    URL = Item.prepare_url('products/vendors')
    SINGLE_URL = Item.prepare_url('products/vendors/%(id)s')

    ORDERING = ('name',)

    def get(self, **kwargs):
        """
        res = client.ProductVendors.get()
        res = client.ProductVendors.get(limit=1, order_by=-name)
        """
        kwargs['url'] = self.URL
        kwargs['allowed_ordering'] = self.ORDERING
        return self.transport.set_method('GET').set_pagination(**kwargs). \
            set_ordering(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        Here _id is category id.

        res = client.ProductVendors.getOne(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('GET').request(**kwargs)


class ProductCampaigns(Item):
    """
    List of campaigns that have products

    Required scope - "products_for_website"
    """
    URL = Item.prepare_url('products/advcampaigns/website/%(id)s')
    SINGLE_URL = Item.prepare_url(
        'products/advcampaigns/%(c_id)s/website/%(id)s')

    ORDERING = ('name',)

    def get(self, _id, **kwargs):
        """
        Here _id is website id.

        res = client.ProductCampaigns.get(22)
        res = client.ProductCampaigns.get(22, limit=1, order_by=-name)
        """
        kwargs['url'] = self.URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['allowed_ordering'] = self.ORDERING
        return self.transport.set_method('GET').set_pagination(**kwargs). \
            set_ordering(**kwargs).request(**kwargs)

    def getOne(self, _id, c_id, **kwargs):
        """
        Here _id is website id and c_id is campaign id

        res = client.ProductCampaigns.getOne(22, 6)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['c_id'] = self.sanitize_id(c_id)
        return self.transport.set_method('GET').request(**kwargs)


class Products(Item):
    """
    List of products

    Required scope - "products_for_website"
    """
    URL = Item.prepare_url('products/website/%(id)s')
    SINGLE_URL = Item.prepare_url('products/%(p_id)s/website/%(id)s')

    ORDERING = ('price', 'category', 'vendor', 'campaign', 'date_updated')
    FILTERING = {
        'keyword': Item.to_unicode,
        'price_from': int,
        'price_to': int,
        'campaign': int,
        'category': int,
        'vendor': int
    }

    def get(self, _id, **kwargs):
        """
        Here _id is website id.

        res = client.Products.get(22)
        res = client.Products.get(22, limit=1)
        res = client.Products.get(22, limit=1, order_by=-price)
        res = client.Products.get(22, price_from=1000)
        """
        kwargs['url'] = self.URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['allowed_ordering'] = self.ORDERING
        kwargs['allowed_filtering'] = self.FILTERING
        return self.transport.set_method('GET').set_pagination(**kwargs).\
            set_filtering(**kwargs).set_ordering(**kwargs).request(**kwargs)

    def getOne(self, _id, p_id, **kwargs):
        """
        Here _id is website id and p_id is product id

        res = client.ProductCampaigns.getOne(22, 2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        kwargs['p_id'] = self.sanitize_id(p_id)
        return self.transport.set_method('GET').request(**kwargs)
