#!/usr/bin/env python
# -*- coding: utf-8 -*-
from apscheduler.schedulers.background import BackgroundScheduler


sched = BackgroundScheduler()


def some_job():
    print('every 10 sec')


sched.add_job(some_job, 'interval', seconds=10)

sched.start()

while True:
    pass