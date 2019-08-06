#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyMetaClass(type):

    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        if "attr" not in attrs:
            attrs['attr'] = True

        return super().__new__(cls, name, bases, attrs)



class TestingMeta(metaclass = MyMetaClass):

    _field = "Field"

    def __init__(self):
        self._var = 100
        self._new_var = 200
