from flask import  Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from security import authenticate, identity
from resources.item import Item, ItemList
from db import db
from resources.store import Store, StoreList
import os

app = Flask(__name__)
uri = os.getenv("DATABASE_URL", "sqlite:///data.db")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'hieu'
api = Api(app)

db.init_app(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister,'/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == "__main__":

    app.run(port=5000, debug=True)
