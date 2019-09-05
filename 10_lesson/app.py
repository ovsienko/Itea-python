from flask import Flask
from flask_restful import Api
from resources.resource import ItemApi
from models.models import Item

app = Flask(__name__)
api = Api(app)


api.add_resource(ItemApi, '/', '/<string:id>')

@app.route('/total')
def total():
    total = 0
    items = Item.objects()
    for item in items:
        total += item.price * item.quantity
    return str(total)

if __name__ == '__main__':
    app.run(debug=True)