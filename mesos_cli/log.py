
import logging
import sys

debug = logging.debug

def fatal(msg, code=1):
    logging.error(msg)
    sys.exit(code)

def fn(f, *args, **kwargs):
    logging.debug("{}: {} {}".format(repr(f), args, kwargs))
    return f(*args, **kwargs)
