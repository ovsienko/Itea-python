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
        return self._mydb

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


def sql_update(query):
    with Db() as mydb:
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()


def is_admin(session):
    if session['isadmin']:
        return True
    else:
        return False


app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route("/")
def index():
    if not session.get('logged_in'):
            return redirect('/login', code=302)
    admin = is_admin(session)
    students = sql_fetchall('''SELECT students.id,
                                    students.name,
                                    students.second_name,
                                    s_group.name,
                                    s_group.faculty,
                                    students.number
                                    FROM students
                                    LEFT JOIN s_group
                                    ON students.s_group = s_group.id ''')
    return render_template('index.html',
                           students=students,
                           admin=admin)


@app.route('/student/<id>')
def student(id):
    if not session.get('logged_in'):
        return redirect('/login', code=302)
    admin = is_admin(session)
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
    marks = sql_fetchall('''SELECT  `subj`, `mark`, id FROM `mark` WHERE `user_id` = %s
        ''' % id)
    return render_template('student.html',
                           student=student,
                           marks=marks,
                           admin=admin)


@app.route('/student/<id>/add-mark', methods=['GET', 'POST'])
def add_mark(id):
    admin = is_admin(session)
    if not session.get('logged_in') or not admin:
        return render_template('add-mark.html', error=True)
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
        sql = '''INSERT INTO `mark` (`subj`, `mark`, `user_id`)
                 VALUES (%s, %s, %s)'''
        val = (form['subj'], form['mark'], student[4])
        sql_insert(sql, val)
        message = 'Оцінку додано! '
    return render_template('add-mark.html',
                           student=student,
                           admin=admin,
                           message=message)


@app.route('/mark/<id>/edit', methods=['GET', 'POST'])
def mark_edit(id):
    admin = is_admin(session)
    if not session.get('logged_in') or not admin:
        return render_template('edit-mark.html', error=True)
    if request.method == "GET":
        query = '''SELECT `id`, `subj`, `mark`, `user_id`
                   FROM `mark`
                   WHERE `id` =  %s ''' % id
        mark = sql_fetchone(query)
        return render_template('edit-mark.html', mark=mark)
    if request.method == "POST":
        form = dict(request.form)
        query = '''UPDATE `mark`
                   SET `mark`={0}
                   WHERE `id` = {1}'''.format(form['mark'], form['id'])
        sql_update(query)
        query = '''SELECT `id`, `subj`, `mark`, `user_id`
                   FROM `mark`
                   WHERE `id` =  %s''' % form['id']
        mark = sql_fetchone(query)
        return render_template('edit-mark.html', mark=mark)


@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    admin = is_admin(session)
    if not session.get('logged_in') or not admin:
        return render_template('edit-mark.html', error=True)
    if request.method == 'GET':
        query = "SELECT `id`, `name`, `faculty` FROM `s_group`"
        groups = sql_fetchall(query)
        return render_template('add-student.html', groups=groups)
    else:
        form = dict(request.form)
        query = '''INSERT INTO `students` (`name`, `second_name`, `s_group`, `number`)
          VALUES (%s, %s, %s, %s)'''
        values = (form['name'],
                  form['second_name'],
                  form['group'],
                  form['number'])
        sql_insert(query, values)
        return redirect('/', code=302)


@app.route('/student/<id>/edit', methods=['GET', 'POST'])
def edit_student(id):
    admin = is_admin(session)
    if not session.get('logged_in') or not admin:
        return render_template('edit-student.html', error=True)
    if request.method == "GET":
        query = '''SELECT `id`, `name`, `second_name`, `s_group`, `number`
                   FROM `students`
                   WHERE `id` =  %s ''' % id
        student = sql_fetchone(query)
        query = "SELECT `id`, `name`, `faculty` FROM `s_group`"
        groups = sql_fetchall(query)
        return render_template('edit-student.html',
                               student=student,
                               groups=groups)
    if request.method == "POST":
        form = dict(request.form)
        query = '''UPDATE `students`
                   SET name="{0}",
                   second_name="{1}",
                   s_group="{2}",
                   number="{3}"
                   where id = {4}'''.format(form['name'],
                                            form['second_name'],
                                            form['group'],
                                            form['number'],
                                            id)
        sql_update(query)
        return redirect('/student/%s/edit' % id, code=302)


@app.route('/add-group', methods=['GET', 'POST'])
def add_group():
    admin = is_admin(session)
    if not session.get('logged_in') or not admin:
        return render_template('add-group.html', error=True)
    if request.method == 'GET':
        return render_template('add-group.html')
    else:
        form = dict(request.form)
        query = '''INSERT INTO `s_group` (`name`, `faculty`) VALUES (%s, %s)'''
        values = (form['name'], form['faculty'])
        sql_insert(query, values)
        return redirect('/add-group', code=302)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if not session.get('logged_in'):
        return redirect('/login', code=302)
    if request.method == 'GET':
        # student =  None
        return render_template('search.html', error=None)
    else:
        form = dict(request.form)
        if form['number']:
            query = '''SELECT `id`, `name`, `second_name`, `s_group`, `number`
                        FROM `students`
                        WHERE `number` = %s''' % form['number']
            student = sql_fetchone(query)
            print(student)
            return render_template('search.html', student=student, error=None)
        else:
            return render_template('search.html', error=True)


@app.route('/top')
def top():
#список студентів по середній оцінці.
    admin = is_admin(session)
    if not session.get('logged_in'):
        return redirect('/login', code=302)
    username = session.get('logged_in')
    students = sql_fetchall('''SELECT students.id,
    students.name,
    students.second_name,
     s_group.name,
    s_group.faculty,
       AVG(mark.mark)
    FROM students
    LEFT JOIN mark
    ON students.id= mark.user_id
    LEFT JOIN s_group
    on students.s_group = s_group.id
    GROUP BY students.id
    ORDER BY AVG(mark.mark) desc ''')
    return render_template('top.html',
                           students=students,
                           admin=admin)


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
            myresult = sql_fetchone('''SELECT password, isadmin
                                    FROM users
                                    where username = %s''' % form['username'])
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
