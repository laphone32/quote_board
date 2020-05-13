#!/usr/bin/env python3

import os, time
from quote import QuoteProvider
from yahoo_finance_quote import YahooFinanceQuoteProvider

class TickerBase:
    def __init__(self, ui, symbols):
        super().__init__()
        self.ui = ui
        self.symbols = symbols
#        self.interval = 1
#
#        filenames = os.path.basename(__file__).split('.')
#        if len(filenames) > 3:
#        # name.position.interval.extension
#            interval = filenames[2]
#        else:
#            # name.interval.extension
#            interval = filenames[1]
#
#        if interval.endswith('s'):
#            self.interval = int(interval[:-1])
#        elif interval.endswith('m'):
#            self.interval = int(interval[:-1]) * 60
#        elif interval.endswith('h'):
#            self.interval = int(interval[:-1]) * 3600

    def refresh(self):
        buff = []
        price = ''
        state = ''
        for symbol, tick in YahooFinanceQuoteProvider().fetch(self.symbols).items():
            price = '%8.2f%10.2f (%6.2f%%)' % (tick.price, tick.priceChange, tick.priceChangePercent)
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

            buff.append('%-10s%s %s' % (symbol, price, state))

        return buff

#        print(buff[int(time.time()) % (len(buff) * self.interval)])
#        print('---')
#        for data in buff:
#            print(data)

