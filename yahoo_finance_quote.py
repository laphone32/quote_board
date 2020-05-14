#!/usr/bin/env python3

import requests
from quote import QuoteProvider

class YahooFinanceQuoteProvider(QuoteProvider):
    __fields="symbol,marketState,shortName,fullExchangeName,quoteType,currency,regularMarketPrice,regularMarketChange,regularMarketChangePercent,preMarketPrice,preMarketChange,preMarketChangePercent,postMarketPrice,postMarketChange,postMarketChangePercent,regularMarketVolume,marketCap,sourceInterval,quoteSourceName"

    def fetch(self, symbols):
        r = requests.get('https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&corsDomain=finance.yahoo.com&fields=' + self.__fields + '&symbols=' + ','.join(symbols)).json()['quoteResponse']['result']

#        print(r)

        ret = {}
        for symbol in r:
            __price = 0.0
            __priceChange = 0.0
            __priceChangePercent = 0.0
            __state = symbol['marketState']
            if ((__state == 'PRE') and ('preMarketChangePercent' in symbol)):
                __state = QuoteProvider.State.Pre
                __price = symbol['preMarketPrice']
                __priceChange = symbol['preMarketChange']
                __priceChangePercent = symbol['preMarketChangePercent']
            elif ((__state != 'REGULAR') and ('postMarketChangePercent' in symbol)):
                __state = QuoteProvider.State.Post
                __price = symbol['postMarketPrice']
                __priceChange = symbol['postMarketChange']
                __priceChangePercent = symbol['postMarketChangePercent']
            else:
                __state = QuoteProvider.State.Open
                __price = symbol['regularMarketPrice']
                __priceChange = symbol['regularMarketChange']
                __priceChangePercent = symbol['regularMarketChangePercent']

            ret.update({symbol['symbol']: QuoteProvider.Info(symbol['shortName'], symbol['fullExchangeName'], __state, symbol['currency'], __price, __priceChange, __priceChangePercent, symbol.get('regularMarketVolume', 0), symbol.get('marketCap', 0), QuoteProvider.Source(symbol.get('quoteSourceName', 'YAHOO'), symbol.get('sourceInterval', 'Unknown'), symbol['quoteType']))})

        return ret

