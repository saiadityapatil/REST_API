from flask_restful import Resource
from schemas.order_schema import OrderSchema
from flask_app.dyno_service import table

schema = OrderSchema()

class OrderResource(Resource):
    def get(self, order_id=None):
        if order_id:
            resp = table.get_item(Key={'PK': f"ORDER#{order_id}", 'SK': f"ORDER#{order_id}"})
            if 'Item' not in resp:
                return {'message': 'Not Found'}, 404
            return resp['Item']
        return ('List not implemented', 400)

    def post(self):
        data = schema.load(request.json)
        pk = f"ORDER#{data['OrderID']}"
        item = {
            'PK': pk, 'SK': pk,
            **data, 'Type': 'Order',
            'CustomerPK': f"CUST#{data['CustomerID']}"
        }
        table.put_item(Item=item)
        return item, 201

    def put(self, order_id):
        data = schema.load(request.json, partial=True)
        key = {'PK': f"ORDER#{order_id}", 'SK': f"ORDER#{order_id}"}
        update = {"AttributeUpdates": {k: {"Value": v, "Action": "PUT"} for k, v in data.items()}}
        table.update_item(Key=key, **update)
        return table.get_item(Key=key).get('Item'), 200
