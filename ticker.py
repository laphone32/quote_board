#!/usr/bin/env python3

from ticker_base import TickerBase
from ascii_ui import AsciiUI
from symbols import symbols

for data in TickerBase(AsciiUI(), symbols).refresh():
    print(data)


