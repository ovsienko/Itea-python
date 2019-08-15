#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
import random
import time


def random_generator(num, thread_name):
    for i in range(num):
        time.sleep(random.randint(0, 5))
        print("I`m executing from", thread_name)


# thread1 = Thread(target=random_generator, args=(5, 'thread1'))
# thread2 = Thread(target=random_generreator, args=(5, 'thread2'))

# thread1.start()
# thread2.start()

# random_generator(5, 'main Thread')

# def file_writer(file_name, num_of_lines):
#     with open(file_name, 'w') as f:
#         for l in range(num_of_lines):
#             f.write(str(random.randint(3323277777777, 5000555555255555555))+'\n')


# list_of_thread = []

# for i in range(10):
#     t = Thread(target=file_writer,
#                 args=('txt/'+str(random.randint(0,100000))+'.txt', random.randint(0, 3055)))
#     #list_of_thread.append(t)
#     t.start()

class RandomGeneretorThread(Thread):
    """docstring for RandomGeneretorThread"""
    def __init__(self, num, name):
        super(RandomGeneretorThread, self).__init__()
        self._num = num
        self._name = name
        Thread.__init__(self, name=self._name)

    def run(self):
        for i in range(self._num):
            time.sleep(random.randint(0, 5))
            print("I`m executing from", self._name)


a = RandomGeneretorThread(10, 'a')
b = RandomGeneretorThread(10, 'b')

a.start()
b.start()
