from marshmallow import Schema, fields

class EmpresaSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)