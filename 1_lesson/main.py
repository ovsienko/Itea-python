# !/usr/bin/env python
# -*- coding: utf-8 -*-

my_list = []
for i in range(100):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)

cap = {
    'Ukraine': 'Kyiv',
    'Poland': 'Warsaw',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'Norway': 'Oslo'}
countryes = ['Poland', 'Canada', 'Spain', 'Moldova']

for x in countryes:
    if cap.has_key(x):
            print(cap[x])
