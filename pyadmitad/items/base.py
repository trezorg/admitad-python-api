class Item(object):

    def __init__(self, transport):
        self.transport = transport

    def sanitize_id(self, item_id):
        if type(item_id) == int:
            return str(item_id)
        return item_id
