from flask import Flask, request
from flask_restful import Api
from flask_app.customer import CustomerResource, CustomerOrderHistory
from flask_app.product import ProductResource
from flask_app.order import OrderResource

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(CustomerResource, '/customers', '/customers/<string:customer_id>')
    api.add_resource(ProductResource, '/products', '/products/<string:product_id>')
    api.add_resource(OrderResource, '/orders', '/orders/<string:order_id>')
    api.add_resource(CustomerOrderHistory, '/customers/<string:customer_id>/orders')
    return app

app = create_app()
