#!/usr/bin/env python3

from enum import Enum

class QuoteProvider:
    class State(Enum):
        Pre = 0
        Open = 1
        Post = 2

    class Info:
        def __init__(self, name, state, currency, price, priceChange, priceChangePercent, volume):
            super().__init__()
            self.name = name
            self.state = state
            self.currency = currency
            self.price = price
            self.priceChange = priceChange
            self.priceChangePercent = priceChangePercent
            self.volume = volume

    def fetch(self, symbols) -> {}:
        pass

