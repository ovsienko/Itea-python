#!/usr/bin/env python
# -*- coding: utf-8 -*-

# list = [1, 2, 3, 4, 5]

# it = list.__iter__()

# print(it.__next__())

# class  A:
#     def __init__(self):
#         self._a = 0
#         self._b = 1

# print(vars(A()))


class NumberGenerator:
    """docstring for NumberGenerator"""
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            self._start += 1
            return self._start
        raise StopIteration("The end of stucture")

a = NumberGenerator(0, 3)

# print(iter(a))
# print(next(a))
# print(iter(a))
# print(next(a))
# print(iter(a))
# print(next(a))
# print(iter(a))
# print(next(a))
# print(iter(a))
# print(next(a))
# print(iter(a))


class MyArray:
    __slots__ = '_size', '_vartype', '_array'

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


    def __len__(self):
        return len(self._array)


arr = MyArray(10, int)
arr[2] = 1
print(len(arr))
for i in arr:
    print(i)