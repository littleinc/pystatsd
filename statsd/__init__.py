from __future__ import absolute_import
import os
import socket

from .client import StatsClient

__all__ = ['StatsClient', 'statsd']

VERSION = (2, 0, 0)
__version__ = '.'.join(map(str, VERSION))

statsd = None
