#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
# a = {'name': 'Pupa',
#      'students': ['Kolya', 'Vasya', 'Petya']}

# b = json.dumps(a, indent=5)
# print(b)
str_j = '{"name": "ABu" }'

ad = json.loads(str_j)
print(ad['name'])