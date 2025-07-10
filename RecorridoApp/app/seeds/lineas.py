import json
import logging

# --- Configuración de logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Datos en crudo ---
LINEAS_ISELIN = [
    {"codigo": "512A", "nombre_ida": "Barrio Cristiano", "nombre_vuelta": "Barrio Union Obrera"},
    {"codigo": "512B", "nombre_ida": "Barrio Cristiano", "nombre_vuelta": "El Cerrito"},
    {"codigo": "513A", "nombre_ida": "Barrio UNIMEV", "nombre_vuelta": "Cementerio por Cordoba"},
    {"codigo": "513B", "nombre_ida": "Barrio Libertad", "nombre_vuelta": "Cementerio por Moreno"},
    {"codigo": "511A", "nombre_ida": "Amapola - Rio Diamante", "nombre_vuelta": "Cuadro Nacional por Sarmiento - Sol de Mayo"},
    {"codigo": "511B", "nombre_ida": "Rama caida - Rio Diamante", "nombre_vuelta": "Cuadro Nacional por Salas"},
    {"codigo": "511C", "nombre_ida": "Los Filtros - El Sosneado", "nombre_vuelta": "Terminal San Rafael"},
    {"codigo": "514A", "nombre_ida": "Barrio Valle Grande - Barrio Docente", "nombre_vuelta": "Cementerio"},
    {"codigo": "514B", "nombre_ida": "Barrio Valle Grande - Barrio Docente", "nombre_vuelta": "Cementerio - El Molino"},
]

LINEAS_BUTTINI = [
    {"codigo": "541", "nombre": "Zanjon Civit"},
    {"codigo": "542", "nombre": "Cuadro Benegas - Pedro Vargas"},
    {"codigo": "543", "nombre": "Pedro Vargas - Los Coroneles"},
    {"codigo": "544", "nombre": "Salto de las Rosas - Colonia Bella Vista - Los Claveles"},
    {"codigo": "547", "nombre": "El Nihuil"},
    {"codigo": "548", "nombre": "Cañada Seca por Cuarteles"},
    {"codigo": "571", "nombre": "Jensen por Dean Funes"},
    {"codigo": "572", "nombre": "El Usillal"},
    {"codigo": "573", "nombre": "Costa Toledano - Colonia Iaccarini"},
    {"codigo": "574", "nombre": "Las Paredes - Montoya - El Cristo"},
    {"codigo": "575", "nombre": "Villa 25 de Mayo"}
]

# --- Formateo a estructura JSON ---
def generar_datos_lineas():
    datos = {
        "lineas": [
            {"empresa": "Iselin", "codigo": l["codigo"], "nombre": l["nombre_ida"], "sentido": "ida"} for l in LINEAS_ISELIN
        ] + [
            {"empresa": "Iselin", "codigo": l["codigo"], "nombre": l["nombre_vuelta"], "sentido": "vuelta"} for l in LINEAS_ISELIN
        ] + [
            {"empresa": "A. Buttini", "codigo": l["codigo"], "nombre": l["nombre"], "sentido": "ida"} for l in LINEAS_BUTTINI
        ] + [
            {"empresa": "A. Buttini", "codigo": l["codigo"], "nombre": "San Rafael", "sentido": "vuelta"} for l in LINEAS_BUTTINI
        ]
    }
    return datos

# --- Ejecución principal ---
if __name__ == "__main__":
    datos_lineas = generar_datos_lineas()
    print(json.dumps(datos_lineas, indent=4, ensure_ascii=False))
    logger.info(f"Se generaron {len(datos_lineas['lineas'])} registros de líneas.")
