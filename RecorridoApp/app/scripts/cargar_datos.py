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
import csv

empresas= [
    {"nombre": "Iselin"},
    {"nombre": "Andesmar"},
    {"nombre": "20 de Junio"},
    {"nombre": "A. Buttini"},
    {"nombre": "Cata"},
    {"nombre": "Chevallier"},
]

origen= "San Rafael"

script_dir = os.path.dirname(__file__)
csv_destinos = os.path.join(script_dir, 'docs', 'data.csv')

destinos = []
with open(csv_destinos, newline='', encoding='utf-8') as csvfile:
    # CSV con separador punto y coma
    lector = csv.DictReader(csvfile, delimiter=';')
    # Limpiar y filtrar nombres de campo
    campos = [fn.strip() for fn in lector.fieldnames if fn and fn.strip()]
    # Verificar columnas requeridas
    if 'nombre' not in campos or 'tiempo_estimado' not in campos:
        logger.error(f"El CSV debe tener columnas 'nombre' y 'tiempo_estimado'. Encontradas: {campos}")
        sys.exit(1)
    for fila in lector:
        nombre = fila.get('nombre')
        tiempo = fila.get('tiempo_estimado')
        if nombre is None or tiempo is None:
            logger.warning(f"Saltando fila incompleta: {fila}")
            continue
        destinos.append({
            'nombre': nombre.strip(),
            'tiempo_estimado': tiempo.strip()
        })
def parse_tiempo(tstr):
    horas, minutos = map(int, tstr.split(':'))
    return timedelta(hours=horas, minutes=minutos)

viajes= []

for empresa in empresas:
    for dest in destinos:
        for i in range(5):
            hora_salida= datetime(2025, 1, 1, random.randint(0, 23), random.choice(range(0, 56,5)))
            tmp_estimado= parse_tiempo(dest["tiempo_estimado"])  
            hora_llegada= hora_salida + tmp_estimado

            hora_salida_vuelta= hora_salida + timedelta(hours= 2, minutes=0) # Salida de vuelta 2 horas después de la llegada
            hora_llegada_vuelta= hora_salida_vuelta + tmp_estimado

            # Definir un costo aleatorio
            costo_aleatorio = random.randint(10000, 30000) 

            viajes.append({
                "empresa": empresa["nombre"],
                "origen": origen,
                "destino": dest["nombre"],
                "hora_salida": hora_salida.strftime("%H:%M"),
                "hora_llegada": hora_llegada.strftime("%H:%M"),
                "costo_base": costo_aleatorio,
            })
            
            viajes.append({
                "empresa": empresa ["nombre"],
                "origen": dest["nombre"],
                "destino": origen,
                "hora_salida": hora_salida_vuelta.strftime("%H:%M"),
                "hora_llegada": hora_llegada_vuelta.strftime("%H:%M"),
                "costo_base": costo_aleatorio,
            })

from app import db, create_app
from app.models import Empresa, Ruta, Viaje
from sqlalchemy import text

app = create_app()

with app.app_context():
    # VACIAR tablas
    db.session.execute(text('TRUNCATE TABLE viaje, ruta, empresa RESTART IDENTITY CASCADE;'))
    db.session.commit()
    logger.info('Tablas truncadas')

    # Insertar empresas
    empresa_ids = {}
    for e in empresas:
        ent = db.session.query(Empresa).filter_by(nombre=e['nombre']).first()
        if not ent:
            ent = Empresa(nombre=e['nombre'])
            db.session.add(ent); db.session.commit()
        empresa_ids[e['nombre']] = ent.id

    # Insertar rutas y viajes
    ruta_map = {}
    for v in viajes:
        # Clave solo con origen y destino para rutas
        key = (v['origen'], v['destino'])
        if key not in ruta_map:
            origen, destino = key
            ruta = Ruta(
                origen=origen,
                destino=destino
            )
            db.session.add(ruta)
            db.session.flush()  # Asigna ruta.id
            ruta_map[key] = ruta.id
       
        # Insertar viaje con horarios y costo
        ruta_id = ruta_map[key]
        empresa_id = empresa_ids[v['empresa']]
        viaje = Viaje(
            ruta_id=ruta_id,
            empresa_id=empresa_id,
            hora_salida=v['hora_salida'],
            hora_llegada=v['hora_llegada'],
            costo_base=v['costo_base']
        )
        db.session.add(viaje)

    try:
        db.session.commit()
        logger.info('Datos cargados correctamente')
    except Exception as err:
        db.session.rollback()
        logger.error(f"Error cargando datos: {err}")