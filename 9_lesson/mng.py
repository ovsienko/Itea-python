#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongoengine import *


connect("students")




class Faculty(Document):
    name = StringField(max_length=30)


class Groupe(Document):
    name = StringField(max_length=30)
    faculty = ReferenceField(Faculty)


class Curator(Document):
    name = StringField(max_length=30)
    surname = StringField(max_length=30)


class Student(Document):
    name = StringField(max_length=30)
    fathersname = StringField(max_length=30)
    surname = StringField(max_length=30)
    groupe = ReferenceField(Groupe)
    curator = ReferenceField(Curator)
    marks = ListField(IntField())




# faculty = Faculty(name='Хімічний')
# faculty.save()
# groupe = Groupe(name='HT-21', faculty=faculty)
# groupe.save()
# curator = Curator(name='Іван', surname='Іванов')
# curator.save()
# student = Student(name="Микола", fathersname='Петрович',
#                   surname='Дикий', groupe=groupe, curator=curator)
# student.marks.append(5)
# student.save()



students = Student.objects(curator__name='Іван').get()
print(students)
# for student in students:
#     print(student.marks)