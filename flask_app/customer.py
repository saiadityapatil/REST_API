from flask_restful import Resource
from schemas.customer_schema import CustomerSchema
from flask_app.dyno_service import table
import boto3

schema = CustomerSchema()

class CustomerResource(Resource):
    def get(self, customer_id=None):
        if not customer_id:
            return ('List not implemented', 400)
        resp = table.get_item(Key={'PK': f"CUST#{customer_id}", 'SK': f"CUST#{customer_id}"})
        item = resp.get('Item')
        if not item:
            return {'message': 'Not Found'}, 404
        return item

    def post(self):
        data = schema.load(request.json)
        pk = f"CUST#{data['CustomerID']}"
        item = {'PK': pk, 'SK': pk, **data, 'Type': 'Customer'}
        table.put_item(Item=item)
        return item, 201

    def put(self, customer_id):
        data = schema.load(request.json, partial=True)
        key = {'PK': f"CUST#{customer_id}", 'SK': f"CUST#{customer_id}"}
        update = {"AttributeUpdates": {k: {"Value": v, "Action": "PUT"} for k, v in data.items()}}
        table.update_item(Key=key, **update)
        resp = table.get_item(Key=key)
        return resp.get('Item'), 200

class CustomerOrderHistory(Resource):
    def get(self, customer_id):
        items = table.query(KeyConditionExpression=boto3.dynamodb.conditions.Key('PK').eq(f"CUST#{customer_id}") & boto3.dynamodb.conditions.Key('SK').begins_with("ORDER#"))
        return {'orders': items.get('Items', [])}
