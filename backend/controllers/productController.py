# backend/controllers/productController.py

from flask import Blueprint, jsonify, request
from .models.productModel import Product

product_api = Blueprint('product_api', __name__)

@product_api.route('/products', methods=['GET'])
def get_products():
    products = Product.objects().to_json()
    return products, 200

@product_api.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.objects.get(id=id).to_json()
    return product, 200
