#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Test:

    def __init__(self, x):
        self._x = x

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")


obj = Test(100)
print(obj.x)
obj.x = 1
print(obj.x)