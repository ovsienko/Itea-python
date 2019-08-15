#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve

db_name = 'local.db'

# with shelve.open(db_name) as db:
#     db["Contry"] = ('Ukraine', 'USA', 'France')

#     for c in db.items():
#         print(c)


def create_item(key, value):
    with shelve.open(db_name) as db:
        db[key] = value


def get_item(key):
    with shelve.open(db_name) as db:
        result = None
        try:
            result = db[key]
        except KeyError:
            return None

        return result


def delete_item(key):
    with shelve.open(db_name) as db:
        return db.pop(key, None)


def clear_db():
    with shelve.open(db_name) as db:
        db.clear()


bar = {'name': 'John', }
create_item('foo', bar)
print(get_item('foo')['name'])

delete_item('foo')
print(get_item('foo'))
