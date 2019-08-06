#!/usr/bin/env python
# -*- coding: utf-8 -*-


B = type('MyClass', (), {'var_in_class': 'yes'})
b = B()
print(b.__dict__)
