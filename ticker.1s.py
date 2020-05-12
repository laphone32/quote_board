#!/usr/bin/env python3

import time
from quote import QuoteProvider
from yahoo_finance_fetcher import YahooFinanceQuoteProvider



symbols = ['GOOG', '2330.TW', '^VIX', 'JPY=X']
x = YahooFinanceQuoteProvider().fetch(symbols)

buff = []
color = ''
state = ''
for symbol, tick in x.items():
    if tick.priceChange > 0:
        color = 'green'
    elif tick.priceChange < 0:
        color = 'red'

    buff.append(symbol + ' <span color=\'' + color + '\'><tt>' + str(tick.price)+ '</tt></span>')


print(buff[int(time.time()) % len(buff)])
print('---')
for data in buff:
    print(data)

