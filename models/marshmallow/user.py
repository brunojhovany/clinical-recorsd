from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    username = fields.Email(required=True)
    password = fields.Str(validate=validate.Length(min=8))
    clinic = fields.Int(required=True)
