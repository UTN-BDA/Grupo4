from marshmallow import Schema, fields

class ViajeSchema(Schema):
    id = fields.Int(dump_only=True)
    ruta_id = fields.Int(required=True)
    empresa_id = fields.Int(required=True)
    hora_salida = fields.Time(required=True)
    hora_llegada = fields.Time(required=True)
    costo_base = fields.Float(required=True)
    ruta = fields.Nested('RutaSchema')
    empresa = fields.Nested('EmpresaSchema')

class RutaSchema(Schema):
    id = fields.Int(dump_only=True)
    origen = fields.Str(required=True)
    destino = fields.Str(required=True)