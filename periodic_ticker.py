#!/usr/bin/ev python3

import os, time
from ticker_base import TickerBase

class PeriodicTicker(TickerBase):
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
        print(buff[int(time.time()) % (len(buff) * self.interval)])
        print('---')
        for data in buff:
            print(data)

