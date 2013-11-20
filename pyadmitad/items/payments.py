from pyadmitad.items.base import Item


__all__ = (
    'Payments',
    'PaymentsManage',
)


class Payments(Item):
    """
    List of webmaster payments

    Required scope - "payments"
    """
    URL = Item.prepare_url('payments')
    SINGLE_URL = Item.prepare_url('payments/%(id)s')

    def get(self, **kwargs):
        """
        res = client.Payments.get()
        res = client.Payments.get(limit=2)

        """
        kwargs['url'] = self.URL
        return self.transport.set_method('GET').set_pagination(**kwargs).request(**kwargs)

    def getOne(self, _id, **kwargs):
        """
        res = client.Payments.getOne(_id=2)
        res = client.Payments.getOne(2)
        """
        kwargs['url'] = self.SINGLE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('GET').request(**kwargs)


class PaymentsManage(Item):
    """
    Manage payments

    Required scope - "manage_websites"
    """

    CREATE_URL = Item.prepare_url('payments/request/%(code)s')
    CONFIRM_URL = Item.prepare_url('payments/confirm/%(id)s')
    DELETE_URL = Item.prepare_url('payments/delete/%(id)s')

    def create(self, _code, **kwargs):
        """
        Create a payment request.
        _code is a code of currency

        res = client.PaymentsManage.create('USD')

        """
        kwargs['url'] = self.CREATE_URL
        kwargs['code'] = self.sanitize_currency(_code)
        return self.transport.set_method('POST').request(**kwargs)

    def confirm(self, _id, **kwargs):
        """
        Confirm a payment request.
        _id is a payment id.

        res = client.PaymentsManage.confirm(71)

        """
        kwargs['url'] = self.CONFIRM_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('POST').request(**kwargs)

    def delete(self, _id, **kwargs):
        """
        Delete a payment request.
        _id is a payment id.

        res = client.PaymentsManage.delete(71)

        """
        kwargs['url'] = self.DELETE_URL
        kwargs['id'] = self.sanitize_id(_id)
        return self.transport.set_method('POST').request(**kwargs)
