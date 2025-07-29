from marshmallow import Schema, fields

class CustomerSchema(Schema):
    CustomerID = fields.Str(required=True)
    CompanyName = fields.Str(required=True)
    ContactName = fields.Str(required=False)
