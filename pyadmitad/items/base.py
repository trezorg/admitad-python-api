from datetime import datetime, date
from pyadmitad.constants import DATE_FORMAT, BASE_URL,\
    CURRENCIES, LONG_DATE_FORMAT


class Item(object):

    def __init__(self, transport):
        self.transport = transport
        self.transport.clean_data()

    def sanitize_id(self, _id, name='_id'):
        return self.sanitize_integer_value(_id, name)

    @staticmethod
    def sanitize_non_blank_value(value, name):
        if not value:
            raise ValueError("Invalid non-blank value '%s': %s" % (name, value))
        return value

    @staticmethod
    def sanitize_string_value(
            value, name, max_length=None, min_length=None, blank=False):
        if not value:
            if not blank:
                raise ValueError(
                    "Invalid string value '%s': %s. Cannot be blank." %
                    (name, value))
            return value
        if max_length and len(value) > max_length:
                raise ValueError(
                    "Invalid string value '%s': %s. Max length: %s" %
                    (name, value, max_length))
        if min_length and len(value) < min_length:
                raise ValueError(
                    "Invalid string value '%s': %s. Min length: %s" %
                    (name, value, min_length))
        return value

    @staticmethod
    def sanitize_integer_value(value, name, blank=False):
        if not value:
            if not blank:
                raise ValueError("Blank integer value '%s': %s" % (name, value))
            return value
        if type(value) == int:
            return str(value)
        elif type(value) == str:
            if value.isdigit():
                return value
        raise ValueError("Invalid integer value '%s': %s" % (name, value))

    @staticmethod
    def sanitize_float_value(value, name, blank=False):
        if not value:
            if not blank:
                raise ValueError("Blank float value '%s': %s" % (name, value))
            return value
        if type(value) in (float, int):
            return str(value)
        elif type(value) == str:
            try:
                float(value)
                return value
            except ValueError:
                raise ValueError("Invalid float value '%s': %s" % (name, value))
        raise ValueError("Invalid float value '%s': %s" % (name, value))

    @staticmethod
    def sanitize_integer_array(values, name, blank=False):
        if not values:
            if not blank:
                raise ValueError(
                    "Blank integer values '%s': %s" % (name, values))
            return values
        return [Item.sanitize_integer_value(x, name, blank=blank)
                for x in values]

    @staticmethod
    def sanitize_string_array(
            values, name, max_length=None, min_length=None, blank=False):
        if not values:
            if not blank:
                raise ValueError(
                    "Blank string values '%s': %s" % (name, values))
            return values
        return [Item.sanitize_string_value(
            x, name, max_length=max_length, min_length=min_length, blank=blank)
            for x in values]

    @staticmethod
    def sanitize_currency(value, blank=True):
        if not value:
            if not blank:
                raise ValueError(
                    "Blank currency value: %s" % value)
            return value
        if value not in CURRENCIES:
                raise ValueError(
                    "Invalid currency value: %s" % value)
        return value

    @staticmethod
    def check_date(dt):
        s = datetime.strptime(dt, DATE_FORMAT).date()
        if s > date.today():
            s = date.today()
        return s.strftime(DATE_FORMAT)

    @staticmethod
    def check_long_date(dt):
        s = datetime.strptime(dt, LONG_DATE_FORMAT)
        if s > datetime.now():
            s = datetime.now()
        return s.strftime(LONG_DATE_FORMAT)

    @staticmethod
    def prepare_url(path):
        url = '%s%s' % (BASE_URL,  path)
        if not url.endswith('/'):
            url += '/'
        return url

    @staticmethod
    def to_unicode(text):
        return u'%s' % text
