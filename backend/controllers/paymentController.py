
# backend/controllers/paymentController.py

import stripe
from flask import Blueprint, request, jsonify
from .models.orderModel import Order
from .models.productModel import Product

stripe_api = Blueprint('stripe_api', __name__)

stripe.api_key = 'your_stripe_secret_key'

@stripe_api.route('/payment/charge', methods=['POST'])
def stripe_charge():
    data = request.get_json()

    try:
        charge = stripe.Charge.create(
            amount=int(data['amount']) * 100,
            currency='usd',
            source=data['token']
        )
        new_order = Order(user=current_user)  # Assuming `current_user` is authenticated
        for item in data['cart']:
            product = Product.objects.get(id=item['id'])
            new_order.products.append(ProductInOrder(product=product, quantity=item['quantity']))
        new_order.save()
        return jsonify(charge), 200
    except stripe.error.StripeError as e:
        return jsonify(error=str(e)), 400
