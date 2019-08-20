#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, request


app = Flask(__name__)



def hello_world():
    students = {'Andry': 34, 'Alice': 99, 'Bob': 98}
    title = 'students list'
    return render_template('index.html', students=students, title=title)


@app.route('/new_route')
def new_route():
    return 'NEW ROUTE'

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index_page():
    print(request)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)

