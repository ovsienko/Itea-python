#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time


def repeat_run_time(repeats):
    def run_time(func):
            def wrapper(**kwargs):
                for i in range(repeats):
                    start = time.time()
                    ip = func()
                    finish = time.time()
                    delta_time = round(finish - start, 2)
                    print("My public ip is {0}. Fetched by function '{1}', on {2} seconds".format(ip, func.__name__, delta_time))
            return wrapper
    return run_time


@repeat_run_time(3)
def get_public_ip():
    try:
        response = requests.get('https://ifconfig.me/ip')
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print('Error code ', e)


get_public_ip()
