#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=["POST"])
def hello_world():
    print(request.json)
    return request.json


if __name__ == '__main__':
    app.run(debug=True)
