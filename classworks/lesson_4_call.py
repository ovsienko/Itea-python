#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A:

    def __init__(self, var):
        self._var = 10

    def __call__(self, *args, **kwargs):
        return self._var


list_var = [(1, 2), (3, 4), (5, 6), (6, 7)]


new_list = [x, y if x not ]