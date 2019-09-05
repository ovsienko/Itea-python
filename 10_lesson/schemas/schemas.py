from marshmallow import fields, Schema, validates, ValidationError


class Category_schema(Schema):
    name = fields.String(required=True, min_lengh=3)
    description = fields.String()
    id = fields.String()


class Item_schema(Schema):
    id = fields.String()
    name = fields.String(required=True)
    price = fields.Int()
    quantity = fields.Int()
    category = fields.Nested(Category_schema)
    is_availiable = fields.Bool(dump_only=True)
    view_count = fields.Int()
