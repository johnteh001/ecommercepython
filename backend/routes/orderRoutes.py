# backend/routes/orderRoutes.py

from flask import Blueprint, jsonify
from .models.orderModel import Order

order_api = Blueprint('order_api', __name__)

@order_api.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.objects().to_json()
    return orders, 200
