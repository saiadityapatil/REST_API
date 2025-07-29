import awsgi
from flask_app.app import app

def lambda_handler(event, context):
    return awsgi.handler(app, event, context)
