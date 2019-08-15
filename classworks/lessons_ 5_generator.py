#!/usr/bin/env python
# -*- coding: utf-8 -*-


def number_generator(numbers):
    for i in range(numbers):
        yield i

a = number_generator(10)

