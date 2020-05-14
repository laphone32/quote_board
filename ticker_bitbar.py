#!/usr/bin/env PYTHONIOENCODING=UTF-8 /Users/jlin/usr/local/bin/python3

from panel_ticker import PanelTicker
from ascii_ui import AsciiUI
from symbols import symbols

PanelTicker(AsciiUI(), symbols).refresh()

