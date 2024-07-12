# backend/models/orderModel.py

from . import db
from .productModel import Product

class ProductInOrder(db.EmbeddedDocument):
    product = db.ReferenceField(Product)
    quantity = db.IntField(default=1)

class Order(db.Document):
    user = db.ReferenceField('User')
    products = db.ListField(db.EmbeddedDocumentField(ProductInOrder))
