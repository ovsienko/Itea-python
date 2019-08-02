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

# car = Automobile()
# bus = Bus()
# car2 = Automobile()
# print(car==car2)
# print(-car)


# addition = lambda x, y: x + y
# print(addition(1, 3))

# list_var = [1, 44, -3, 33, 234, -94]
# map_var = filter(lambda x: x % 2 == 0, list_var)
# print(map_var)

# class Singltone:

#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#             return cls._instance
#         else:
#             raise Exception('Instance alresy exist')
# class Singletone:

#     _instance = None  # Keep instance reference

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance

# class Singletone:

#     _instance = None  # Keep instance reference

#     def new(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().new(cls)
#         return cls._instance

# class A(Singletone):
#     pass

# a1 = A()
# a2 = A()

# print(a1 is a2)

def s(a, b=0, c = 1):
    pass

s(2, b=3, c= 9)


# def f(*args, **kwargs):
#     print(args)
#     print(kwargs)

# f(1, 2, '44', b='a', pidor='You')