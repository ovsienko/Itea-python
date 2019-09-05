from flask_restful import Resource
from flask import request
from schemas.schemas import Category_schema, Item_schema
from models.models import Category, Item


class ItemApi(Resource):

    def get(self, id=None):
        if not id:
            return Item_schema(many=True).dump(Item.objects())
        else:
            item = Item.objects.get(id=id)
            item.view_count += 1
            item.save()
            return Item_schema().dump(item)

    def post(self):
        err = Item_schema().validate(request.json)
        if err:
            raise ValueError(err)
        print(request.json)
        itm_obj = Item(**request.json).save()
        return Item_schema().dump(itm_obj)

    def put(self, id):
        err = Item_schema().validate(request.json)
        if err:
            raise ValueError(err)
        itm_obj = Item.objects.get(id=id)
        itm_obj.update(**request.json)
        itm_obj.save()
        return Item_schema().dump(itm_obj)

    def delete(self, id):
        Item.objects.get(id=id).delete()
        return 'Deleted'