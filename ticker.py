#!/usr/bin/env python3

from ticker_base import TickerBase
from ascii_ui import AsciiUI


symbols = ['GOOG', '2330.TW', '^VIX', 'JPY=X']

for data in TickerBase(AsciiUI(), symbols).refresh():
    print(data)


