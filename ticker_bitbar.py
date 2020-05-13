#!/usr/bin/env PYTHONIOENCODING=UTF-8 /Users/jlin/usr/local/bin/python3

from periodic_ticker import PeriodicTicker
from ascii_ui import AsciiUI

symbols = ['GOOG', '2330.TW', '^VIX', 'JPY=X']
PeriodicTicker(AsciiUI(), symbols).refresh()

