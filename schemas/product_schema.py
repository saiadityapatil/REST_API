from marshmallow import Schema, fields

class ProductSchema(Schema):
    ProductID = fields.Int(required=True)
    ProductName = fields.Str(required=True)
    UnitPrice = fields.Float(required=False)
