import sys

PY3 = sys.version_info[0] == 3

if PY3:
    def iteritems(d, **kw):
        return iter(d.items(**kw))
    string_types = str
else:
    def iteritems(d, **kw):
        return iter(d.iteritems(**kw))
    string_types = basestring
