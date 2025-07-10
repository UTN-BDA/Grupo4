from marshmallow import Schema, fields

class ParadaSchema(Schema):
    id = fields.Int(dump_only=True)
    ubicacion = fields.Str(required=True)
    latitud = fields.Float(required=True)
    longitud = fields.Float(required=True)
    detalles_referencia = fields.Str(required=True)

class ParadaConLineasSchema(Schema):
    id = fields.Int(dump_only=True)
    ubicacion = fields.Str(required=True)
    latitud = fields.Float(required=True)
    longitud = fields.Float(required=True)
    detalles_referencia = fields.Str(required=True)
    lineas = fields.List(fields.Nested('LineaBasicaSchema'))