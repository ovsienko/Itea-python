#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyDict:

    def __init__(self):
        self._dict = {}

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __getitem__(self, key):
        return self._dict[key]

    def get(self, key, default=None):
        try:
            return self._dict[key]
        except:
            return default

    def items(self):
        result = []
        for i in self._dict:
            result.append((i, self._dict[i]))
        return result

    def keys(self):
        result = []
        for i in self._dict:
            result.append(i)
        return result

    def values(self):
        result = []
        for i in self._dict:
            result.append(self._dict[i])
        return result

    def __add__(self, other):
        f = MyDict()
        for i in self.keys():
            f[i] = self[i]
        for i in other.keys():
            f[i] = other[i]
        return f


d = MyDict()
d['foo'] = 'bar'
d['second'] = 2
print(d['foo'])
print(d.get('foooo', 'Niet'))
print(d.items())
print(d.keys())
print(d.values())
c = MyDict()
c['spam'] = 'buy viagra online'
c['nice'] = True
a = d + c
print(a.items())
