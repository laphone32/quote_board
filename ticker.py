#!/usr/bin/env python3

from quote import QuoteProvider
from yahoo_finance_fetcher import YahooFinanceQuoteProvider

symbols = ['GOOG', '2330.TW', '^VIX', 'JPY=X']
x = YahooFinanceQuoteProvider().fetch(symbols)

color = ''
state = ''
for symbol, tick in x.items():
    if tick.priceChange > 0:
        color = '\033[32m'
    elif tick.priceChange < 0:
        color = '\033[31m'

    if tick.state == QuoteProvider.State.Pre:
        state = '+'
    elif tick.state == QuoteProvider.State.Post:
        state = '*'

    print ('%-10s\033[1;37m%s%8.2f%10.2f (%6.2f%%)\033[00m %s' % (symbol, color, tick.price, tick.priceChange, tick.priceChangePercent, state))

