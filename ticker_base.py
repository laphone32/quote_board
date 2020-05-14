#!/usr/bin/env python3

import os, time
from quote import QuoteProvider
from yahoo_finance_quote import YahooFinanceQuoteProvider

class TickerBase:
    def __init__(self, ui, symbols):
        super().__init__()
        self.ui = ui
        self.symbols = symbols

    def refresh(self):
        buff = []
        price = ''
        state = ''
        for symbol, tick in YahooFinanceQuoteProvider().fetch(self.symbols).items():
            price = '%8.2f%8.2f (%.1f%%)' % (tick.price, tick.priceChange, tick.priceChangePercent)
            if tick.priceChange > 0:
                price = self.ui.upward(price)
            elif tick.priceChange < 0:
                price = self.ui.downward(price)

            if tick.state == QuoteProvider.State.Pre:
                state = '+'
            elif tick.state == QuoteProvider.State.Post:
                state = '*'
            else:
                state = ''

            buff.append((symbol, tick, '%-10s%s %s' % (symbol, price, state)))

        return buff

