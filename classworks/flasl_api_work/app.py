#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from resources import test_resource
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(test_resource.Test, '/', '/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
