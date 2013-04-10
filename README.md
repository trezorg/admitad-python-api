admitad-python-api
==================

A Python wrapper around the Admitad API

Install
-------

Dependencies

* requests
* simplejson

PyAdmitad is not yet available on PyPI, we're waiting to have it a bit more
stable. Install by cloning from the GitHub repo:

    $ git clone git://github.com/trezorg/admitad-python-api.git
    $ cp -r admitad-python-api/pyadmitad path/to/destination


Example
-------

    from pyadmitad import api

    client_id = ""
    client_secret = ""
    username = ""
    password = ""
    scope = "private_data"

    client = api.get_oauth_password_client(
        client_id,
        client_secret,
        username,
        password,
        scope
    )

    print client.Me.get()

Notes
------

It is possible to override the default response handler by passing handler as
a keyword argument to a client function call. For example:

    x = lambda x, y: (x, y)
    result = client.Me.get(handler=x)
