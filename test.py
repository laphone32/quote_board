#!/usr/bin/env python3

from yahoo_finance_fetcher import YahooFinanceQuoteProvider

symbols = ['AAPL', '2330.TW', '^VIX', 'JPY=X']
x = YahooFinanceQuoteProvider().fetch(symbols)

print(x)

print(x['2330.TW'].name)

