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


class Bus(Automobile):
    _seats = 40
    _wheels = 6

    def beep(self):
        print("BEEP-BEEP")


class Truck(Automobile):
    _seats = 3
    _cargo = 30000

    def get_cargo(self):
        return self._cargo

    def beep(self):
        print("Beep, motherfucker!")\



auto = Automobile()
print(auto.get_seats())
print(auto.get_wheels())
auto.beep()

bus = Bus()
print(bus.get_seats())
print(bus.get_wheels())
print(bus.get_engine())
print(bus.get_electro())
bus.beep()

truck = Truck()
print("Truck`s cargo ", truck.get_cargo())
truck.beep()
