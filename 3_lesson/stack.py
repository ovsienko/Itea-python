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
