#!/usr/bin/ev python3

import os, time
from ticker_base import TickerBase


# output used for bitbar and argos plugin
class PanelTicker(TickerBase):
    def __init__(self, ui, symbols):
        super().__init__(ui, symbols)
        self.interval = 1

        filenames = os.path.basename(__file__).split('.')
        if len(filenames) > 3:
        # name.position.interval.extension
            interval = filenames[2]
        else:
            # name.interval.extension
            interval = filenames[1]

        if interval.endswith('s'):
            self.interval = int(interval[:-1])
        elif interval.endswith('m'):
            self.interval = int(interval[:-1]) * 60
        elif interval.endswith('h'):
            self.interval = int(interval[:-1]) * 3600

    def refresh(self):
        buff = super().refresh()
        print(buff[int(time.time()) % (len(buff) * self.interval)][2])
        print('---')
        for data in buff:
            print(data[2])
            tick = data[1]
            print('--%s' % (tick.name))
            print('--%s @ %s' % (data[0], tick.exchange))
            print('--volume: %s (%s %s)' % (tick.volume, tick.marketCap, tick.currency))
            print('-----')
            print('--source: %s' % tick.source.name)
            print('--type: %s' % tick.source.type)
            print('--interval: %s' % tick.source.interval)
