from flask_restful import Resource
from schemas.product_schema import ProductSchema
from flask_app.dyno_service import table

schema = ProductSchema()

class ProductResource(Resource):
    def get(self, product_id=None):
        if product_id:
            resp = table.get_item(Key={'PK': f"PROD#{product_id}", 'SK': f"PROD#{product_id}"})
            if 'Item' not in resp:
                return {'message': 'Not Found'}, 404
            return resp['Item']
        return ('List not implemented', 400)

    def post(self):
        data = schema.load(request.json)
        pk = f"PROD#{data['ProductID']}"
        item = {'PK': pk, 'SK': pk, **data, 'Type': 'Product'}
        table.put_item(Item=item)
        return item, 201

    def put(self, product_id):
        data = schema.load(request.json, partial=True)
        key = {'PK': f"PROD#{product_id}", 'SK': f"PROD#{product_id}"}
        update = {"AttributeUpdates": {k: {"Value": v, "Action": "PUT"} for k, v in data.items()}}
        table.update_item(Key=key, **update)
        return table.get_item(Key=key).get('Item'), 200
