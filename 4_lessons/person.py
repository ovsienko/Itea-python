#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Создайте класс ПЕРСОНА с абстрактными методами, 
# позволяющими вывести на экран информацию о персоне, 
# а также определить ее возраст (в текущем году). 
# Создайте дочерние классы: 
# АБИТУРИЕНТ (фамилия, дата рождения, факультет), 
# СТУДЕНТ (фамилия, дата рождения, факультет, курс), 
# ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж), 
# со своими методами вывода информации на экран и определения возраста. 
# Создайте список из n персон, выведите полную информацию из базы на экран, 
# а также организуйте поиск персон, чей возраст попадает в заданный диапазон.


from abc import abstractmethod, ABC
import datetime
now = datetime.datetime.now()

class Person(ABC):

    @abstractmethod
    def __init__(self, second_name, birthday, faculty):
        self._second_name = second_name
        self._birthday = birthday
        self.faculty = faculty
    
    def age(self):
        now = datetime.datetime.now()
        age = now.year - self._birthday
        return age

    @property
    def second_name(self):
        return self._second_name

    @property
    def faculty(self):
        return self._faculty

    @abstractmethod
    def print_person(self):
        print(self.second_name, self.age(), self.faculty)


class Entrant(Person):

    def __init__(self, second_name, birthday, faculty):
        self._second_name = second_name
        self._birthday = birthday
        self._faculty = faculty

    def print_person(self):
        print(self.second_name, self.age(), self.faculty)


en = Entrant('Shevxhenko', 1987, 'Phisic')

en.print_person()