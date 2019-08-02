#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stack:

    def __init__(self, max_size):
        self._items = []
        self._max_size = max_size

    def size(self):
        return len(self._items)

    def get_items(self):
        return self._items

    def isFull(self):
        if self.size() >= self._max_size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, item):
        if self.isFull():
            print('Stack is full')
        else:
            self._items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self._items.pop()
        else:
            print('Stack alredy empty')

    def top(self):
        return self._items[-1]

    def clear(self):
        self._items.clear()


class Queue(Stack):

    def pop(self):
        if not self.isEmpty():
            return self._items.pop(0)
        else:
            print('Queue alredy empty')

    def push(self, item):
        if self.isFull():
            print('Queue is full')
        else:
            self._items.append(item)

    def top(self):
        if not self.isEmpty:
            return self._items[0]


stack = Stack(5)
print('Stack is empty ', stack.isEmpty())
stack.push(1)
print('Stack is empty ', stack.isEmpty())
stack.push(2)
stack.push(3)
stack.isFull()
print(stack.top())
stack.push(23)
stack.push(1)
print(stack.size())

q = Queue(5)
for x in range(1, 7):
    q.push(x)

for x in range(1, 7):
    print(q.pop())
q.push('32')
print(q.get_items())
q.push('32')
print(q.get_items())


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