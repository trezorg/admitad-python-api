

class HttpException(Exception):
    def __init__(self, status, content):
        self.status = status
        self.content = content

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "HttpException(%s): %s" % (self.status, self.content)


class ConnectionException(Exception):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "ConnectionException(%s): %s" % self.content


class JsonException(Exception):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "JsonException: %s" % self.content


class ApiException(Exception):
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "ApiException(%s): %s" % self.content
