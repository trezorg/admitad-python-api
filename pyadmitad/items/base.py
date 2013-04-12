class Item(object):

    def __init__(self, transport):
        self.transport = transport

    def sanitize_id(self, _id):
        if type(_id) == int:
            return str(_id)
        elif type(_id) == str:
            if _id.isdigit():
                return _id
        raise ValueError("Wrong _id value: %s" % _id)

    def sanitize_non_blank_value(self, value, name):
        if not value:
            raise ValueError("Wrong non-blank value %s: %s" % (name, value))
        return value
