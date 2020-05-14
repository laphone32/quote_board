#!/usr/bin/env python3

from enum import Enum

class QuoteProvider:
    class State(Enum):
        Pre = 0
        Open = 1
        Post = 2

    class Source:
        def __init__(self, name, interval, quoteType):
            super().__init__()
            self.name = name
            self.interval = interval
            self.type = quoteType

    class Info:
        def __init__(self, name, exchange, state, currency, price, priceChange, priceChangePercent, volume, marketCap, source):
            super().__init__()
            self.name = name
            self.exchange = exchange
            self.state = state
            self.currency = currency
            self.price = price
            self.priceChange = priceChange
            self.priceChangePercent = priceChangePercent
            self.volume = volume
            self.marketCap = marketCap
            self.source = source

    def fetch(self, symbols) -> {}:
        pass

