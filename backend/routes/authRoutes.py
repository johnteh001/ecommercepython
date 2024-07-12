# backend/routes/authRoutes.py

from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from .models.userModel import User
import jwt

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.objects(username=data['username']).first()

    if user and check_password_hash(user.password, data['password']):
        token = jwt.encode({'username': user.username}, 'your_secret_key')
        return jsonify({'token': token.decode('UTF-8')}), 200

    return jsonify({'message': 'Invalid credentials!'}), 401
