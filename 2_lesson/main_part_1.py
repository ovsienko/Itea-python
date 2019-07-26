#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal:
    name = "Gav"
    animals_created = 0
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        Animal.animals_created += 1

    def move(self):
        print('I`m moving')

    def eat(self):
        print('I`m eating')

    def sleep(self):
        print('I`m sleeping')

    def who_am_i(self):
        print('I`m the {0}. My type is {1}'.format(self.name, self.animal_type))
        print(self.__class__)

    def __del__(self):
        print('Instance is deleted from memmory ')


animal_object = Animal('Human', 'Mammal')

animal_object1 = Animal('H', 'M')

print(Animal.animals_created)