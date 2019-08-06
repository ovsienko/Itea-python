#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


def run_time(func):
        def wrapper(**kwargs):
                start = time.time()
                func()
                finish = time.time()
                delta_time = round(finish - start, 2)
                print(delta_time)
        return wrapper


@run_time
def creare_list():
    my_list = []
    for x in range(100000000):
        my_list.append(x)


@run_time
def creare_list_comp():
    my_list = [x for x in range(100000000)]


creare_list()
creare_list_comp()
