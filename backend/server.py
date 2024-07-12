# backend/server.py

from flask import Flask
from flask_cors import CORS
from .config.db import db
from .routes.adminRoutes import admin_api
from .routes.orderRoutes import order_api
from .routes.productRoutes import product_api
from .routes.authRoutes import auth_api
from .controllers.paymentController import stripe_api
from .middleware.authMiddleware import auth_api as auth_middleware_api

app = Flask(__name__)
CORS(app)

# Configuration
app.config['MONGODB_SETTINGS'] = {
    'db': 'ecommerce',
    'host': 'mongodb://localhost/ecommerce'
}
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize MongoDB
db.init_app(app)

# Register Blueprints
app.register_blueprint(admin_api, url_prefix='/api/admin')
app.register_blueprint(order_api, url_prefix='/api/order')
app.register_blueprint(product_api, url_prefix='/api/product')
app.register_blueprint(auth_api, url_prefix='/api/auth')
app.register_blueprint(stripe_api, url_prefix='/api/payment')
app.register_blueprint(auth_middleware_api)

if __name__ == '__main__':
    app.run(debug=True)
