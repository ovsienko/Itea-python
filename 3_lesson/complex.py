#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def notation(self):
        if self.a != 0:
            pr_a = str(self.a)
        else:
            pr_a = ''
        if self.b < 0:
            pr_b = str(self.b) + 'i'
        elif self.b > 0 and self.a != 0:
            pr_b = '+' + str(self.b) + 'i'
        elif self.b > 0 and self.a == 0:
            pr_b = str(self.b) + 'i'
        else:
            pr_b = ''
        return(pr_a + pr_b)

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return ComplexNumber(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b,
                             self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        a = (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)
        b = (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)
        return ComplexNumber(a, b)


for a in range(-20, 30):
    for b in range(-20, 34):
        z1 = ComplexNumber(a, b)
        z2 = ComplexNumber(b, a)
        print('z1 is', z1.notation())
        print('z2 is', z2.notation())
        plus = z1 + z2
        print(z1.notation(), '+', z2.notation(), '=', plus.notation())
        minus = z1 - z2
        print(z1.notation(), '-', z2.notation(), '=', minus.notation())
        mul = z1 * z2
        print(z1.notation(), '*', z2.notation(), '=', mul.notation())
        try:
            div = z1 / z2
            print(z1.notation(), '/', z2.notation(), '=', div.notation())
        except ZeroDivisionError:
            print('ZeroDivisionError: division by zero')
        print('#' * 25)
