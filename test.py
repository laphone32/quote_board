#!/usr/bin/env python3

from yahoo_finance_quote import YahooFinanceQuoteProvider
from symbols import symbols

x = YahooFinanceQuoteProvider().fetch(symbols)

print(x)

print(x['2330.TW'].name)

