#!/usr/bin/env python3

from ui import UI

class AsciiUI(UI):
    def upward(self, text):
        super().upward(text)
        return '\033[32m' + text + '\033[0m'

    def downward(self, text):
        super().downward(text)
        return '\033[31m' + text + '\033[0m'
