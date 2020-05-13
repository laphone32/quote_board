#!/usr/bin/env python3

from periodic_ticker import PeriodicTicker
from ascii_ui import AsciiUI

symbols = ['GOOG', '2330.TW', '^VIX', 'JPY=X']
PeriodicTicker(AsciiUI(), symbols).refresh()

