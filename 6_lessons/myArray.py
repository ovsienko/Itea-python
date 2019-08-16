#!/usr/bin/env python
# -*- coding: utf-8 -*-
class MyArray:

    def __init__(self, size, vartype):
        self._size = size
        self._vartype = vartype
        self._array = [0] * self._size

    def __getitem__(self, idx):
        if idx > self._size - 1:
            raise StopIteration('Out of range')
        return self._array[idx]

    def __setitem__(self, idx, value):
        # if isinstance(value, self._value) and idx < self._size:
        if isinstance(value, self._vartype) and idx < self._size:
            self._array[idx] = value
        else:
            raise TypeError('Invalid type')

    def pop(self, idx=-1):
        if idx > self._size - 1:
            raise StopIteration('Out of range')
        if idx == -1:
            idx = self._size - 1
        value = self._array[idx]
        rm = []
        for i in range(len(self._array)):
            if i != idx:
                rm.append(self._array[i])
        self._array = rm
        self._size -= 1
        return value

    def append(self, value):
        self._size += 1
        self._array += [value, ]
        return self._array

    def remove(self, value):
        rm = []
        count = 0
        for i in self._array:
            if i == value and count == 0:
                count += 1
            else:
                rm.append(i)
        self._array = rm
        return self._array

    def clear(self):
        self.__init__(self._size, self._vartype)

    def __add__(self, other):
        new_arr = []
        for i in self._array:
            new_arr.append(i)
        for i in other:
            new_arr.append(i)
        return(new_arr)

