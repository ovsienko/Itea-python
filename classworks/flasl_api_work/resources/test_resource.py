from flask_restful import Resource
from flask import request
from schema.test_schema import Item, Category
from models.test_models import Item as Item_model


class Test(Resource):
    def get(self, id=None):
        return Item(many=True).dump(Item_model.objects())

    def post(self):
        error = Category().validate(request.json)
        return error
        print('post request is here')

    def put(self, id=None):
        print('put request is here')

    def delete(self, id=None):
        print('delete request is here')

