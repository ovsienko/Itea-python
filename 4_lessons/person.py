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

    @property
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
        print(self.second_name, self.age, self.faculty)


en = Entrant('Shevchenko', 1987, 'Phisic')
en.print_person()


class Student(Entrant):

    def __init__(self, second_name, birthday, faculty, year):
        Entrant.__init__(self, second_name, birthday, faculty)
        self._year = year

    @property
    def year(self):
        return(self._year)

    def print_person(self):
        print(self.second_name, self.age, self.faculty, self.year)


student = Student('Smith', 1988, 'Phisic', 1)
student.print_person()


class Teacher(Entrant):

    def __init__(self, second_name, birthday, faculty, position, experience):
        Entrant.__init__(self, second_name, birthday, faculty)
        self._position = position
        self._experience = experience

    @property
    def position(self):
        return self._position

    @property
    def experience(self):
        return self._experience

    def print_person(self):
        print(self.second_name, self.age,
              self.faculty, self.position, self.experience)


teacher = Teacher('Holms', 1977, 'Medic', 'senior teacher', 3)
teacher.print_person()

teachers = []
teachers.append(Teacher('Holms', 1977, 'Medic', ' teacher', 8))
teachers.append(Teacher('Li', 1987, 'Medic', 'Professor', 3))
teachers.append(Teacher('Barns', 1970, 'Medic', 'Doctor', 12))
teachers.append(Teacher('Simpsons', 1967, 'Medic', 'teacher', 6))
teachers.append(Teacher('Abu', 1945, 'Medic', ' teacher', 13))
print('#' * 25)
for teacher in teachers:
    teacher.print_person()


def get_person_by_age_range(persons, min_age, max_age):
    return [person for person in persons if min_age < person.age < max_age]


print('#' * 25)
teachers_list = get_person_by_age_range(teachers, 30, 50)
for teacher in teachers_list:
    teacher.print_person()
