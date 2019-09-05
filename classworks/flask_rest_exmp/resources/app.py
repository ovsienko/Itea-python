from flask import Flask
from flask_restful import Api
from resources.employess_resource import EmployeeAPI
app = Flask(__name__)
api = Api(app)


api.add_resource(EmployeeAPI, "/employee", "/employee/<string:id>")



if __name__ == '__main__':
    app.run(debug=True)
