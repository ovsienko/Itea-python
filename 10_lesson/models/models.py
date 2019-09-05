from mongoengine import  *
connect('shop')

class Category(EmbeddedDocument):
    name = StringField(max_length=50)
    description = StringField(max_length=255)

class Item(Document):
    name = StringField(max_length=50)
    price = IntField()
    category = EmbeddedDocumentField(Category)
    quantity = IntField()
    view_count = IntField(default=0)

    @property
    def is_availiable(self):
        if self.quantity > 0:
            return  True
        else:
            return False

