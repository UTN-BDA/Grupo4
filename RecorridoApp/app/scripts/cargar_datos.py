# Script de prueba.
import sys
import os
import logging
from datetime import datetime, timedelta
import random

# Configurar el logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Asegurarse de que el directorio raíz del proyecto esté en el path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Importar dependencias
from app import db, create_app
app= create_app()
from app.models import Empresa
from app.models import Ruta
from app.models import Viaje    

empresas= [
    {"nombre": "Iselin"},
    {"nombre": "Andesmar"},
    {"nombre": "20 de Junio"},
    {"nombre": "A. Buttini"},
    {"nombre": "Cata"},
    {"nombre": "Chevallier"},
]

origen= "San Rafael"

destino=[
    {"nombre": "Mendoza", "tiempo_estimado": "3:15"},
    {"nombre": "San Luis", "tiempo_estimado": "4:10"},
    {"nombre": "La Rioja", "tiempo_estimado": "9:00"},
    {"nombre": "Buenos Aires", "tiempo_estimado": "15:00"},
    {"nombre": "Neuquen", "tiempo_estimado": "8:00"},
    {"nombre": "San Juan", "tiempo_estimado": "5:40"},
    {"nombre": "Cordoba", "tiempo_estimado": "10:30"},
    {"nombre": "Santa Fe", "tiempo_estimado": "15:10"},
    {"nombre": "Rosario", "tiempo_estimado": "12:55"},
    {"nombre": "Tucuman", "tiempo_estimado": "17:10"},
    {"nombre": "Salta", "tiempo_estimado": "18:00"},
    {"nombre": "Mar del Plata", "tiempo_estimado": "16:00"},
    {"nombre": "Ushuaia", "tiempo_estimado": "74:00"},
    {"nombre": "Comodoro Rivadavia", "tiempo_estimado": "26:50"},
    {"nombre": "Puerto Madryn", "tiempo_estimado": "20:10"},
    {"nombre": "Misiones", "tiempo_estimado": "20:00"},
    {"nombre": "Corrientes", "tiempo_estimado": "19:30"},
    {"nombre": "Formosa", "tiempo_estimado": "16:00"},
    {"nombre": "Chaco", "tiempo_estimado": "14:00"},
    {"nombre": "Entre Rios", "tiempo_estimado": "16:00"},
    {"nombre": "La Pampa", "tiempo_estimado": "7:00"},
]

def parse_tiempo(tstr):
    horas, minutos = map(int, tstr.split(':'))
    return timedelta(hours=horas, minutes=minutos)

viajes= []

for empresa in empresas:
    for dest in destino:
        for i in range(5):
            hora_salida= datetime(2025, 1, 1, random.randint(0, 23), random.choice(range(0, 56,5)))
            tmp_estimado= parse_tiempo(dest["tiempo_estimado"])  
            hora_llegada= hora_salida + tmp_estimado

            viajes.append({
                "empresa": empresa["nombre"],
                "origen": origen,
                "destino": dest["nombre"],
                "hora_salida": hora_salida.strftime("%H:%M"),
                "hora_llegada": hora_llegada.strftime("%H:%M"),
            })

# … tu código de generación de 'viajes' …

from flask import Flask
from sqlalchemy.exc import IntegrityError
from app import db, create_app
from app.models import Empresa, Ruta, Viaje

app = create_app()
app.app_context().push()

# 1) Asegurarse de que todas las empresas existan
empresa_map = {}
for e in empresas:
    nombre = e["nombre"]
    # intenta recuperar...
    obj = Empresa.query.filter_by(nombre=nombre).first()
    if not obj:
        obj = Empresa(nombre=nombre)
        db.session.add(obj)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            obj = Empresa.query.filter_by(nombre=nombre).first()
    empresa_map[nombre] = obj.id

# 2) Insertar rutas y viajes
ruta_map = {}
for v in viajes:
    key = (v["origen"], v["destino"], v["hora_salida"], v["hora_llegada"])
    # 2.a) Ruta: crea sólo si no existe
    if key not in ruta_map:
        origen, destino, hs, hl = key
        ruta = Ruta(
            origen=origen,
            destino=destino,
            hora_salida=hs,
            hora_llegada=hl
        )
        db.session.add(ruta)
        try:
            db.session.flush()      # para obtener ruta.id sin hacer commit completo
        except IntegrityError:
            db.session.rollback()
            ruta = Ruta.query.filter_by(
                origen=origen,
                destino=destino,
                hora_salida=hs,
                hora_llegada=hl
            ).first()
        ruta_map[key] = ruta.id

    ruta_id = ruta_map[key]
    empresa_id = empresa_map[v["empresa"]]

    # 2.b) Viaje: puedes asignar un costo_base según tu lógica; aquí, un random de ejemplo
    costo_base = round(random.uniform(1000, 5000), 2)

    viaje = Viaje(
        ruta_id=ruta_id,
        empresa_id=empresa_id,
        costo_base=costo_base
    )
    db.session.add(viaje)

# 3) Commit final
try:
    db.session.commit()
    logger.info("Se han insertado todas las rutas y viajes correctamente.")
except Exception as e:
    db.session.rollback()
    logger.error("Error al insertar datos: %s", e)
