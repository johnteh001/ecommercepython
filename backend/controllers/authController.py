# backend/controllers/authController.py

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .models.userModel import User

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password, email=data['email'])
    new_user.save()
    return jsonify({'message': 'User created successfully!'}), 201

@auth_api.route('/login', methods=['POST'])
def login_user():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Could not verify'}), 401

    user = User.objects(username=auth.username).first()

    if not user:
        return jsonify({'message': 'User not found!'}), 401

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.username}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')}), 200

    return jsonify({'message': 'Invalid password!'}), 401
