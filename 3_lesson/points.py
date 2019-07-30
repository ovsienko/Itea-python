#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Point:

    _x = None

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")

    _y = None

    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y

    def del_y(self):
        del self._y

    y = property(get_y, set_y, del_y, "I'm the 'y' property.")

    _z = None

    def set_z(self, z):
        self._z = z

    def get_z(self):
        return self._z

    def del_z(self):
        del self._z

    z = property(get_z, set_z, del_z, "I'm the 'z' property.")

    def __init__(self, x, y, z):
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)

    def print_axes(self):
        print(self.get_x(), self.get_y(), self.get_z())

    def __add__(self, other):
        return Point(self.get_x() + other.get_x(), self.get_y() + other.get_y(), self.get_z() + other.get_z())

    def __sub__(self, other):
        return Point(self.get_x() - other.get_x(), self.get_y() - other.get_y(), self.get_z() - other.get_z())

    def __mul__(self, other):
        return Point(self.get_x() * other.get_x(), self.get_y() * other.get_y(), self.get_z() * other.get_z())

    def __div__(self, other):
        return Point(self.get_x() / other.get_x(), self.get_y() / other.get_y(), self.get_z() / other.get_z())

    def __neg__(self):
        return Point(-(self.get_x()), -(self.get_y()), -(self.get_z())) 


poin = Point(1, 2, 3)
yet_point = Point(4, 5, 6)
# poin.print_axes()
plus = poin + yet_point
plus.print_axes()
minus = poin - yet_point
minus.print_axes()
mul = poin * yet_point
mul.print_axes()
div = poin / yet_point
div.print_axes()
negativ = -poin
negativ.print_axes()
