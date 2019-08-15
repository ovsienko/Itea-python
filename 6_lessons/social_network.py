#!/usr/bin/env python
# -*- coding: utf-8 -*
import shelve
import os
import datetime

USERS_DB = 'users.db'
POSRTS_DB = 'posts.db'


def get_user(username):
    with shelve.open(USERS_DB) as db:
        result = None
        try:
            result = db[username]
        except KeyError:
            return None
        return result


def get_users():
    with shelve.open(USERS_DB) as db:
        keys = list(db.keys())
        return keys

def create_user(username, values):
    with shelve.open(USERS_DB) as db:
        try:
            if username in db:
                raise Exception('USer already exist')
            else:
                db[username] = values

        except Exception as e:
            print(e)


def get_posts(username):
    with shelve.open(POSRTS_DB) as db:
        try:
            return db[username]
        except:
            return []

def add_post(username, post):
    posts = get_posts(username)
    posts.append(post)
    with shelve.open(POSRTS_DB) as db:
        db[username] = posts


class Registration:

    def __init__(self):

        self._username = ''
        self._passwd = ''
        self._passwd1 = ''
        self._reg_date = ''

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def passwd(self):
        return self._passwd

    @passwd.setter
    def passwd(self, value):
        self._passwd = value

    @property
    def passwd1(self):
        return self._passwd1

    @passwd1.setter
    def passwd1(self, value):
        self._passwd1 = value

    @property
    def reg_date(self):
        return self._reg_date.strftime("%d-%m-%Y %H:%M")

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        self._is_admin = value

    @reg_date.setter
    def reg_date(self, value):
        self._reg_date = value

    def check_username(self):
        if get_user(self.username):
            raise Exception('username already exist')
        elif len(self.username) < 3:
            raise Exception('username is too short')
        else:
            return True

    def check_passwd(self):
        if self.passwd != self.passwd1:
            raise Exception('PAssword is not Match')
        elif len(self.passwd) < 6:
            raise Exception('Password is too short')
        else:
            return True

    def run(self):
        print('Registration!')
        self.username = input('Enter username: ')
        self.passwd = input('Enter password: ')
        self.passwd1 = input('Repear password: ')
        self.reg_date = datetime.datetime.now()
        self.is_admin = False

        try:
            self.check_username()
            self.check_passwd()
            user = [self.username, self.passwd, self.reg_date, self.is_admin]
            create_user(self.username, user)
            return User(self.username)

        except Exception as e:
            os.system('clear')
            print(e)
            self.run()


class Authorization(Registration):

    def __init__(self):
        print('Authorization!')
        self._username = input('Enter username: ')
        self._passwd = input('Enter password: ')

    def run(self):
        try:
            user = get_user(self.username)
            if not get_user(self.username):
                raise Exception('User don`t exist')
            elif user[1] != self.passwd:
                raise Exception('Wrong password')
            else:
                print('Hello,', self.username)
                return User(self.username)
        except Exception as e:
            print(e)


class User:

    def __init__(self, username):
        self._username = username
        user = get_user(username)
        self._is_admin = user[3]

    @property
    def username(self):
        return self._username

    @property
    def is_admin(self):
        return self._is_admin

    def add_post(self):
        text = input('Type your post: ')
        post = (text, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
        add_post(self.username, post)
        self.run()

    def list_posts(self):
        if self.is_admin:
            users = get_users()
            for i in users:
                user = get_user(i)
                prt = 'User {0}, registered: {1}'.format(user[0], user[2])
                print(prt)
                posts = get_posts(i)
                for post in posts:
                    prt = '       {0}: {1}'.format(post[1], post[0])
                    print(prt)
        else:
            posts = get_posts(self.username)
            for post in posts:
                prt = '{0}: {1}'.format(post[1], post[0])
                print(prt)
        self.run()

    def run(self):
        menu = '''
            1. add post
            2. list post
            0. Exit
        '''
        print(menu)
        ch = input('Select action: ')
        if ch == '1':
            self.add_post()
        elif ch == '2':
            self.list_posts()
        elif ch == '0':
            del self
        else:
            self.run()


welcome = '''
Welcome to Python`s Social Network!
1. Login
2. Register
0. Exit
'''
if not get_user('admin'):
    create_user('admin',
               ['admin', '123456', datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), True])
    print('admin created')
user = None

while True:
    print(welcome)
    choice = input('Select: ')
    if choice == '0':
        break
    elif choice == '2':
        user = Registration().run()
    elif choice == '1':
        user = Authorization().run()
    else:
        print('Wrong choice')
    if user:
        user.run()
