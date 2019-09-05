#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongoengine import *
connect("lesson31211")


class User(Document):
    login = StringField(max_length=30)
    password = StringField(min_length=8)
    email = EmailField(unique=True)
    role = StringField()


class Category(Document):
    title = StringField(max_length=255, unique=True)
    description = StringField(max_length=1024)


class Item(Document):

    added_by = ReferenceField(User)
    category = ReferenceField(Category)
    is_available = BooleanField(default=True)
    name = StringField(required=True, max_length=255)
    description = StringField(max_length=2048, required=False)
    weight = FloatField(required=False)






user = {"login": "test_user", "password":"dasdasdasdas",
        "email": "asasA@ukr.net", "role": "admin"}

user_obj = User(**user)
user = user_obj.save()

category = {"title": "Fruits",
            "description": "There gonna be fruits"}

category_obj = Category(**category)
category = category_obj.save()

item = {"added_by": user, "category": category,
        "is_available":True, "name":"orange"}

item = Item(**item).save()
print(item)

items = Item.objects()
for i in items:
    print(i.category.title)


