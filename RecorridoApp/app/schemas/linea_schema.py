from marshmallow import Schema, fields

class LineaBasicaSchema(Schema):
    id = fields.Int(dump_only=True)
    codigo = fields.Str(required=True)
    nombre = fields.Str(required=True)
    frecuencia = fields.Int(required=True)

class LineaSchema(Schema):
    id = fields.Int(dump_only=True)
    codigo = fields.Str(required=True)
    nombre = fields.Str(required=True)
    empresa_id = fields.Int(required=True)
    frecuencia = fields.Int(required=True)
    empresa = fields.Nested('EmpresaSchema')

class LineaConRecorridoSchema(Schema):
    id = fields.Int(dump_only=True)
    codigo = fields.Str(required=True)
    nombre = fields.Str(required=True)
    frecuencia = fields.Int(required=True)
    empresa = fields.Nested('EmpresaSchema')
    recorrido = fields.List(fields.Nested('ParadaConOrdenSchema'))

class ParadaConOrdenSchema(Schema):
    id = fields.Int(dump_only=True)
    ubicacion = fields.Str(required=True)
    latitud = fields.Float(required=True)
    longitud = fields.Float(required=True)
    detalles_referencia = fields.Str(required=True)
    orden = fields.Int(required=True)