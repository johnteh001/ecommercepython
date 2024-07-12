# backend/models/productModel.py

from . import db

class Product(db.Document):
    title = db.StringField(required=True)
    description = db.StringField()
    image_url = db.StringField()
    sizes = db.ListField(db.StringField())
    price = db.DecimalField(required=True, precision=2)
