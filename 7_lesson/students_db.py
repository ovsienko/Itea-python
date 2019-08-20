#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector
from flask import Flask, session, redirect, render_template, request


class Db:

    def __init__(self):
        self._host = 'localhost'
        self._user = 'stdb'
        self._password = '6C713aI1f9qgQ8g7@'
        self._database = 'university'
        self._mydb = mysql.connector.connect(host=self._host,
                                             user=self._user,
                                             passwd=self._password,
                                             database=self._database)

    
    def __enter__(self):
        return  self._mydb


    def __exit__(self, *args):
        self._mydb.close()


def sql_fetchall(query):
    with Db() as mydb:
        mycursor = mydb.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
    return myresult


def sql_fetchone(query):
    with Db() as mydb:
        mycursor = mydb.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchone()
    return myresult


def sql_insert(query, val):
    with Db() as mydb:
        mycursor = mydb.cursor()
        mycursor.execute(query, val)
        mydb.commit()


app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route("/")
def index():
    if not session.get('logged_in'):
        return redirect('/login', code=302)
    username = session.get('logged_in')
    students = sql_fetchall('''SELECT students.id,
                                    students.name,
                                    students.second_name,
                                    s_group.name,
                                    s_group.faculty,
                                    students.number
                                    FROM students
                                    LEFT JOIN s_group
                                    ON students.s_group = s_group.id ''')
    return render_template('index.html', username=username, students=students)


@app.route('/student/<id>')
def student(id):
    if not session.get('logged_in'):
        return redirect('/login', code=302)
    if session['isadmin']:
        admin = True
    else:
        admin = False
    student = sql_fetchone('''SELECT students.name,
                                    students.second_name,
                                    s_group.name,
                                    s_group.faculty,
                                    students.number,
                                    students.id
                                    FROM students
                                    LEFT JOIN s_group
                                    ON students.s_group = s_group.id
                                    WHERE students.id = %s ''' % id)
    marks = sql_fetchall('''SELECT  `subj`, `mark` FROM `mark` WHERE `user_id` = %s
        ''' % id)
    return render_template('student.html',
                           student=student,
                           marks=marks,
                           admin=admin)


@app.route('/student/<id>/add-mark', methods=['GET', 'POST'])
def add_mark(id):
    if session['isadmin']:
        admin = True
    else:
        admin = False
    if not session.get('logged_in') or not admin:
        error = "Вам потрібно залогинитись під обліковим записом що має право на цю дію!"
        return render_template('add-mark.html', error=error)

    student = sql_fetchone('''SELECT students.name,
                                    students.second_name,
                                    s_group.name,
                                    s_group.faculty,
                                    students.id
                                    FROM students
                                    LEFT JOIN s_group
                                    ON students.s_group = s_group.id
                                    WHERE students.id = %s ''' % id)
    message = ''
    if request.method == 'POST':
        form = dict(request.form)
        sql = "INSERT INTO `mark` (`subj`, `mark`, `user_id`) VALUES (%s, %s, %s)"
        val = (form['subj'], form['mark'], student[4])
        sql_insert(sql, val)
        message = 'Оцінку додано! '
    return render_template('add-mark.html', student=student, admin=admin, message=message)

def search():
    pass


def excellent():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        error = ''
        form = dict(request.form)
        if form['username'] == '':
            error = 'Enter your login!'
        elif form['password'] == '':
            error = 'Enter your password'
        else:
            myresult = sql_fetchone('SELECT password, isadmin FROM users where username = "%s" ' % form['username'])
        if not myresult:
            error = 'username not found'
        elif myresult[0] != form['password']:
            error = 'Password not match'
        else:
            session['logged_in'] = form['username']
            if myresult[1] == 1:
                session['isadmin'] = True
            else:
                session['isadmin'] = False
            return redirect('/', code=302)
        return render_template('login.html', sql=myresult, error=error)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return login()


if __name__ == "__main__":
    app.run(debug=True)
