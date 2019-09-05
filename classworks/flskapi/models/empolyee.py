#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *
from constants import SALARY_CHOICES

connect('empoyees')


class Role(EmbeddedDocument):
    name = StringField()
    grade = StringField()
    experience = IntField(min_value=1)


class Salary(Document):
    type = StringField(choices=SALARY_CHOICES)
    amount = IntField(min_value=3200, requred=True)
    fees = IntField(requred=True)
    comment = StringField(max_lenght=2048)

    @property
    def net_salary(self):
        return self.amount - self.fees

    @property
    def commentary(self):
        return self.comment

    @commentary.setter
    def commentary(self, value):
        if isinstance(value, str):
            self.comment = value
        else:
            raise TypeError("Wrong type")


class Employee(Document):
    name = StringField(max_lenght=255)
    surname = StringField(max_lenght=255)
    mail = EmailField()
    salary_payments = ListField(ReferenceField(Salary))
    role = EmbeddedDocumentField(Role)

Employee.objects()