# backend/routes/productRoutes.py

from flask import Blueprint, jsonify
from .models.productModel import Product

product_api = Blueprint('product_api', __name__)

@product_api.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(title=data['title'], description=data['description'], image_url=data['image_url'], sizes=data['sizes'], price=data['price'])
    new_product.save()
    return jsonify({'message': 'Product added successfully!'}), 201

