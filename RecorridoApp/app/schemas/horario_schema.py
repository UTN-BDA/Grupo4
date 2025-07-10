from marshmallow import Schema, fields

class HorarioSchema(Schema):
    id = fields.Int(dump_only=True)
    linea_parada = fields.Int(required=True)
    hora = fields.Time(required=True)
    tipo_dia = fields.Str(required=True)

class HorarioConLineaSchema(Schema):
    id = fields.Int(dump_only=True)
    hora = fields.Time(required=True)
    tipo_dia = fields.Str(required=True)
    linea = fields.Nested('LineaBasicaSchema')
    proxima_llegada = fields.Str(dump_only=True)  # Calculado