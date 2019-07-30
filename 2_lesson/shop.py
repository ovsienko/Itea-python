#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Shop:
    _total = 0

    def __init__(self, name, sells):
        self.name = name
        self.sells = sells
        Shop._total += sells

    def get_total(self):
        return self._total

    def set_sells(self, sells):
        self.sells += sells
        Shop._total += sells
    total = property(get_total, None, None, 'total')


achan = Shop('Achan', 100)
print(achan.sells)
achan.set_sells(10)
print(achan.sells)
print(achan.get_total())
atb = Shop('ATB', 3)
print(atb.sells)
print(atb.get_total())
print(atb.total)