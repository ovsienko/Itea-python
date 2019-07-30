#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Automobile:
    _seats = 4
    _wheels = 4
    _engine = 'V8'
    _electro = False

    def get_seats(self):
        return self._seats

    def set_seats(self, seats):
        self._seats = seats

    def get_wheels(self):
        return self._wheels

    def get_engine(self):
        return self._engine

    def get_electro(self):
        return self._electro

    def beep(self):
        print('Beep!')

    def __eq__(self, other):
        return self.__class__ == other.__class__

    def __neg__(self):
        return self.get_seats() * (-1)


class Bus(Automobile):
    _seats = 40
    _wheels = 6

    def beep(self):
        print("BEEP-BEEP")

car = Automobile()
bus = Bus()
car2 = Automobile()
print(car==car2)
print(-car)