# backend/routes/adminRoutes.py

from flask import Blueprint, jsonify
from .middleware.authMiddleware import token_required

admin_api = Blueprint('admin_api', __name__)

@admin_api.route('/admin/dashboard', methods=['GET'])
@token_required
def admin_dashboard(current_user):
    if current_user.username == 'admin':  # Example check for admin access
        return jsonify({'message': 'Welcome to Admin Dashboard!'}), 200
    else:
        return jsonify({'message': 'Unauthorized access!'}), 403
