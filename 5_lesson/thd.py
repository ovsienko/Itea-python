#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
import requests
from lxml.html import fromstring
# # Создать функцию, которая будет скачивать файл из интернета по ссылке,
# повесить на неё созданный декоратор.
# #Создать список из 10 ссылок, по которым будет происходить скачивание.
# Создать список потоков, отдельный поток, на каждую из ссылок.
#  Каждый поток должен сигнализировать,
#   о том, что, он начал работу и по какой ссылке он работает,
#   так же должен сообщать когда скачивание закончится.

urls = ['https://realpython.com/intro-to-python-threading/',
         'https://python-scripts.com/threading',
            'https://web.telegram.org',
            'https://google.com',
            'http://facebook.com',
            'https://www.cia.gov',
            'https://www.fbi.gov',
            'https://www.privat24.ua',
            'http://olx.ua',
            'https://itea.ua/uk/', ]


def make_tread_var(url, daemon=False):
    def my_tread(func):
        def wraper(*args, **kwargs):
            return Thread(target=func, args=(url,), daemon=daemon, name=url)
        return wraper
    return my_tread

treads = []
for url in urls:
    @make_tread_var(url)
    def get_title(url):
            r = requests.get(url)
            tree = fromstring(r.content)
            title = tree.findtext('.//title')
            print(title)
            print(url, ' is done')
    treads.append(get_title(url))

for thred in treads:
    if not thred.is_alive():
        thred.start()
        print(thred.name, 'is stared')

##### Шось дуже жахливи код. Формально воно відповідає завданню але мені не подобається.
# Киньте лінк як треба було.