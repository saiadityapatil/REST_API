from marshmallow import Schema, fields

class OrderSchema(Schema):
    OrderID = fields.Int(required=True)
    CustomerID = fields.Str(required=True)
    OrderDate = fields.Date(required=False)
