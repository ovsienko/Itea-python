#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class BaseCar(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        print('Stop')
        return True


class Car(BaseCar):
    _x = None

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")
    
    def __init__(self):
        self._engine = "V8"

    def move(self):
        print('Wrumm')

    def stop(self):
        super().stop()
        print('!!')


a = Car()
a.stop()