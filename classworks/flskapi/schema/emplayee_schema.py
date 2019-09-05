#!/usr/bin/env python
# -*- coding: utf-8 -*-

from marshmallow import Schema, fields, validates, ValidationError
from models.empolyee import Employee, Salary, Role


class SalarySchema(Schema):
    class Meta:
        model = Salary


class RoleSchema(Schema):
    pass


class EmployeeScema(Schema):

    class Meta:
        model =  Employee
