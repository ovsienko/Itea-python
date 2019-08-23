#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongoengine import *
connect('lesson9')


class User(Document):
    login = StringField(max_lenght=255)
    password = StringField(min_lenght=255)
    email = EmailField(unique=True)
    role = StringField()

class Category(Document):
    title = StringField(max_lenght=255, unique=True)
    description = StringField()


class Item(Document):
    added_by=ReferenceField(User)
    category = ReferenceField(Category)
    is_available = BooleanField(default=True)
    name = StringField(required=True, max_lenght=255)
    description = StringField(required=True, max_lenght=255)

# user_obj = User(login='Petya', password='1qazXSW@#EDC', email='ksdkd@kdsv.ds', role='kkkk')
# user_obj.save()

# cat = Category(title='Vegetable', description='This is Vegetable')
# cat.save()
# item = Item(added_by=user_obj, category=cat, is_available=True, name='Potato', description='Potato is cool!')
# item.save()
item = Item(name='Potato')
print(item.description)