#!/usr/bin/env python
# -*- coding: utf-8 -*-
from marshmallow import Schema, fields, validates, ValidationError


class Category(Schema):
    id = fields.Str()
    name = fields.Str()


class Item(Schema):
    id = fields.Str()
    name = fields.Str(required=True)
    description = fields.Str()
    category = fields.Nested(Category)

    @validates('name')
    def validate_name(self, value):
        if len(value) < 5:
            raise ValidationError('name is short')
        