import sys

# --------------------------------------------------------------------
# python 3 migration

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY3:
    _iteritems = "items"
    _itervalues = "values"
else:
    _iteritems = "iteritems"
    _itervalues = "itervalues"


def iteritems(d, **kw):
    """Return an iterator over the (key, value) pairs of a dictionary."""
    return iter(getattr(d, _iteritems)(**kw))


def itervalues(d, **kw):
    """Return an iterator over the values of a dictionary."""
    return iter(getattr(d, _itervalues)(**kw))


def binary(v):
    """Return an binary or str."""
    return v.encode("utf-8")
