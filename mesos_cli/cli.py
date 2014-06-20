
import argparse
import blessings
import logging
logging.basicConfig()

from . import config
from . import master

def init(parser):
    cfg = config.Config()
    args = parser.parse_args()

    m = master.state(cfg.master)
    return (cfg, args, m)

def parser(**kwargs):
    return argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        **kwargs
    )

def header(name):
    term = blessings.Terminal()
    print "==>" + term.red + name + term.white + "<=="