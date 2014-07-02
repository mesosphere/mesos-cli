
import mesos.cli

with open("README.rst") as f:
  readme = f.read()

requires = [
    "argcomplete>=0.8.0",
    "blessings>=1.5.1",
    "gevent>=1.0.1",
    "importlib>=1.0.3", # py26
    "kazoo>=2.0",
    "ordereddict>=1.1", # py26
    "prettytable>=0.7.2",
    "protobuf>=2.5.0",
    "requests>=2.2.1"
]

config = {
    'name': 'mesos.cli',
    'version': mesos.cli.__version__,
    'description': 'Mesos CLI Tools',
    'long_description': readme,
    'author': 'Thomas Rampelberg',
    'author_email': 'thomas@mesosphere.io',
    'url': 'http://pypi.python.org/pypi/mesos.cli',
    'license': 'Apache 2.0',
    'keywords': 'mesos',
    'classifiers': [ ],

    'namespace_packages': [ 'mesos' ],
    'packages': [ 'mesos', 'mesos.cli' ],
    'entry_points': {
        'console_scripts': [
            'mesos = mesos.cli.main:main',

            # helpers
            'mesos-completion = mesos.cli.completion:main',
            'mesos-config = mesos.cli.config:main',
            'mesos-resolve = mesos.cli.resolve:main',
            'mesos-state = mesos.cli.state:main',

            # coreutils
            'mesos-cat = mesos.cli.cat:main',
            'mesos-find = mesos.cli.find:main',
            'mesos-head = mesos.cli.head:main',
            'mesos-help = mesos.cli.help:main',
            'mesos-ls = mesos.cli.ls:main',
            'mesos-ps = mesos.cli.ps:main',
            'mesos-scp = mesos.cli.scp:main',
            'mesos-ssh = mesos.cli.ssh:main',
            'mesos-tail = mesos.cli.tail:main'
        ]
    },
    'setup_requires': [
        "nose>=1.3.3",
        "tox>=1.7.1"
    ],
    'install_requires': requires,
    'tests_require': [
        'coverage>=3.7.1',
        'mock>=1.0.1',
        'testtools>=0.9.35', # py26
        'zake>=0.0.20'
    ],
    'test_suite': 'nose.collector',
    'scripts': [
        'bin/mesos-zsh-completion.sh'
    ]
}

from setuptools import setup

setup(**config)
