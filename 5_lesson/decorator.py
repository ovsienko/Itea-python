#!/usr/bin/env python
# -*- coding: utf-8 -*-
 # Создать декоратор, который будет запускать функцию в отдельном потоке.
 #Декоратор должен принимать следующие аргументы:
    # название потока, является ли поток демоном
import random
import time
from threading import Thread


def make_tread_var(name, daemon):
    def my_tread(func):
        def wraper(*args, **kwargs):
            t = Thread(target=func, args=(), daemon=daemon, name=name)
            t.start()
            print('Thread {0} is started'.format(t.name))
        return wraper
    return my_tread

for i in range(10):
    @make_tread_var(i, True)
    def yet_func():
        rnd = random.randint(0, 5)
        print('Wait %s seconds' % rnd)
        time.sleep(rnd)


    yet_func()
