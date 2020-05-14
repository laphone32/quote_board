#!/usr/bin/env python3

from panel_ticker import PanelTicker
from ascii_ui import AsciiUI
from symbols import symbols

PanelTicker(AsciiUI(), symbols).refresh()

