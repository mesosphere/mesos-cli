
import argparse
import blessings
import logging
import os

from . import config
from .master import current as master

def init(parser=None):
    cfg = config.Config()
    args = parser.parse_args() if parser else None

    logging.basicConfig(level=getattr(logging, cfg.level.upper()))

    return (cfg, args)

def parser(**kwargs):
    return argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        **kwargs
    )

def header(name):
    term = blessings.Terminal()
    print "==>" + term.red + str(name) + term.white + "<=="

def cmds(short=False):
    def fltr(cmd):
        if not cmd.startswith("mesos-"):
            return False
        if cmd.endswith(".sh"):
            return False
        return True

    cmds = []
    for path in os.environ.get("PATH").split(os.pathsep):
        try:
            cmds += filter(fltr, os.listdir(path))
        except OSError:
            pass

    if short:
        cmds = [x.split("-", 1)[-1] for x in cmds]

    return cmds

def task_completer(prefix, parsed_args, **kwargs):
    return [x.id for x in master.tasks(prefix)]

