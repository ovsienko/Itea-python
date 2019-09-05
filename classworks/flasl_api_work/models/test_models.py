from mongoengine import *

connect('lessons10')


class Category(EmbeddedDocument):
    name = StringField()

    # @property
    # def item(self):
    #     return Item.objects(category=self)


class Item(Document):
    name = StringField()
    description = StringField()
    category = EmbeddedDocumentField(Category)

cat = Category(name='Vegi').save()
item = Item(name='Tomat', description='Bka bla', category=cat, category).save()
PowerEdge R640