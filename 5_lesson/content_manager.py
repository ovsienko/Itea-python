#!/usr/bin/env python
# -*- coding: utf-8 -*-


class OpenFile:

    def __init__(self, filename, operation):
        self._filename = filename
        self._operation = operation

    def __enter__(self):
        self.f = open(self._filename, self._operation)
        return self.f

    def __exit__(self, *args):
        self.f.close()
        return args


with OpenFile('some.txt', 'w') as f:
    f.write('Hello! \n')

with OpenFile('some.txt', 'r') as f:
    print(f.read())

