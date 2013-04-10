from pyadmitad import items


class FailedRequest(Exception):

    def __init__(self, error):
        self.error = error

    def __str__(self):
        return repr(self.error)


class Client(object):
    """The API client."""

    def __init__(self, transport):
        self.transport = transport

    def __getattr__(self, name):
        return getattr(items, name)(self.transport)
