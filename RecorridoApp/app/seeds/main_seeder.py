"""
Este archivo genera un JSON con todos los datos necesarios para poblar la base de datos
"""

import json
import os
from datetime import datetime

class GeneradorDatosTransporte:
    """Generador de datos realistas para el sistema de transporte de San Rafael"""
    
    def __init__(self):
        self.datos_completos = {
            "empresas": [],
            "paradas": [],
            "lineas": [],
            "linea_paradas": [],
            "horarios": [],
            "rutas": [],
            "viajes": []
        }
        
    def generar_empresas(self):
        """Genera las empresas de transporte"""
        self.datos_completos["empresas"] = [
            {"nombre": "Iselin S.R.L."},
            {"nombre": "A. Buttini e Hijos S.R.L."}
        ]
        
    def generar_paradas(self):
        """Genera todas las paradas del sistema urbano"""
        paradas_data = [
            # ZONA CENTRO
            {"ubicacion": "Terminal San Rafael", "latitud": -34.6177, "longitud": -68.3301, 
             "detalles_referencia": "Terminal de ómnibus - Av. Balloffet y Mitre"},
            {"ubicacion": "Plaza San Martín", "latitud": -34.6158, "longitud": -68.3307, 
             "detalles_referencia": "Plaza central - Av. San Martín y Belgrano"},
            {"ubicacion": "Municipalidad", "latitud": -34.6143, "longitud": -68.3289, 
             "detalles_referencia": "Palacio Municipal - Av. San Martín 175"},
            {"ubicacion": "Hospital Schestakow", "latitud": -34.6089, "longitud": -68.3245, 
             "detalles_referencia": "Hospital público - Av. San Martín Norte"},
            {"ubicacion": "Centro Cívico", "latitud": -34.6123, "longitud": -68.3278, 
             "detalles_referencia": "Edificios gubernamentales - Belgrano y Córdoba"},
            {"ubicacion": "Banco Nación", "latitud": -34.6165, "longitud": -68.3295, 
             "detalles_referencia": "Sucursal central - Av. San Martín y Salta"},
            {"ubicacion": "Supermercado Libertad", "latitud": -34.6167, "longitud": -68.3334, 
             "detalles_referencia": "Supermercado céntrico - Av. San Martín"},
            {"ubicacion": "Estación YPF Centro", "latitud": -34.6134, "longitud": -68.3289, 
             "detalles_referencia": "Estación de servicio céntrica"},
            # ZONA NORTE
            {"ubicacion": "Cementerio Municipal", "latitud": -34.6045, "longitud": -68.3189, 
             "detalles_referencia": "Cementerio San Rafael - Ruta 144 Norte"},
            {"ubicacion": "Barrio UNIMEV", "latitud": -34.5987, "longitud": -68.3156, 
             "detalles_referencia": "Barrio UNIMEV - Acceso Norte"},
            {"ubicacion": "Universidad Nacional", "latitud": -34.5945, "longitud": -68.3089, 
             "detalles_referencia": "UNCuyo Sede San Rafael"},
            {"ubicacion": "Barrio Valle Grande", "latitud": -34.5923, "longitud": -68.3123, 
             "detalles_referencia": "Centro del Barrio Valle Grande"},
            {"ubicacion": "Barrio Docente", "latitud": -34.5901, "longitud": -68.3087, 
             "detalles_referencia": "Barrio Docente - Zona residencial"},
            {"ubicacion": "Los Filtros", "latitud": -34.5834, "longitud": -68.3201, 
             "detalles_referencia": "Zona Los Filtros - Ruta Provincial 144"},
            {"ubicacion": "Acceso Norte", "latitud": -34.5789, "longitud": -68.3234, 
             "detalles_referencia": "Rotonda de acceso norte a la ciudad"},
            # ZONA SUR
            {"ubicacion": "Barrio Unión Obrera", "latitud": -34.6345, "longitud": -68.3245, 
             "detalles_referencia": "Barrio Unión Obrera - Zona Sur"},
            {"ubicacion": "El Cerrito", "latitud": -34.6456, "longitud": -68.3456, 
             "detalles_referencia": "Barrio El Cerrito - Acceso Sur"},
            {"ubicacion": "Barrio Cristiano", "latitud": -34.6389, "longitud": -68.3198, 
             "detalles_referencia": "Barrio Cristiano - Zona Sur"},
            {"ubicacion": "Barrio Libertad", "latitud": -34.6298, "longitud": -68.3387, 
             "detalles_referencia": "Barrio Libertad - Moreno Sur"},
            {"ubicacion": "Acceso Sur Ruta 143", "latitud": -34.6567, "longitud": -68.3234, 
             "detalles_referencia": "Acceso sur por Ruta Nacional 143"},
            # ZONA ESTE
            {"ubicacion": "Río Diamante", "latitud": -34.5723, "longitud": -68.2987, 
             "detalles_referencia": "Acceso al Río Diamante - Zona Este"},
            {"ubicacion": "Cuadro Nacional", "latitud": -34.6156, "longitud": -68.2845, 
             "detalles_referencia": "Cuadro Nacional - Ruta 143"},
            {"ubicacion": "Rama Caída", "latitud": -34.6234, "longitud": -68.2789, 
             "detalles_referencia": "Zona Rama Caída - Este San Rafael"},
            {"ubicacion": "Las Paredes", "latitud": -34.6234, "longitud": -68.2456, 
             "detalles_referencia": "Las Paredes - Distrito Este"},
            {"ubicacion": "Puente Río Diamante", "latitud": -34.5945, "longitud": -68.2756, 
             "detalles_referencia": "Puente sobre Río Diamante"},
            # ZONA OESTE
            {"ubicacion": "Villa 25 de Mayo", "latitud": -34.6234, "longitud": -68.3678, 
             "detalles_referencia": "Villa 25 de Mayo - Zona Oeste"},
            {"ubicacion": "Zanjón Civit", "latitud": -34.6178, "longitud": -68.3789, 
             "detalles_referencia": "Zona Zanjón Civit - Oeste"},
            {"ubicacion": "Cuadro Benegas", "latitud": -34.6298, "longitud": -68.3987, 
             "detalles_referencia": "Cuadro Benegas - Rural Oeste"},
            {"ubicacion": "Pedro Vargas", "latitud": -34.6445, "longitud": -68.4123, 
             "detalles_referencia": "Pedro Vargas - Zona Rural"},
            {"ubicacion": "Los Coroneles", "latitud": -34.6567, "longitud": -68.4234, 
             "detalles_referencia": "Los Coroneles - Distrito Rural"},
            {"ubicacion": "Bella Vista", "latitud": -34.6123, "longitud": -68.3998, 
             "detalles_referencia": "Barrio Bella Vista - Zona Oeste"},
            {"ubicacion": "Claveles", "latitud": -34.6089, "longitud": -68.4056, 
             "detalles_referencia": "Barrio Claveles - Zona Oeste"},
            # ZONAS ALEJADAS/RURALES
            {"ubicacion": "El Nihuil", "latitud": -34.7123, "longitud": -68.4567, 
             "detalles_referencia": "Dique El Nihuil - Zona Turística"},
            {"ubicacion": "Jensen", "latitud": -34.5678, "longitud": -68.4123, 
             "detalles_referencia": "Jensen - Distrito Rural Norte"},
            {"ubicacion": "Cañada Seca", "latitud": -34.6789, "longitud": -68.3987, 
             "detalles_referencia": "Cañada Seca - Zona Rural Sur"},
            {"ubicacion": "Salto de las Rosas", "latitud": -34.5987, "longitud": -68.4456, 
             "detalles_referencia": "Salto de las Rosas - Atractivo Turístico"},
            {"ubicacion": "El Usillal", "latitud": -34.5456, "longitud": -68.4567, 
             "detalles_referencia": "El Usillal - Zona Rural Norte"},
            {"ubicacion": "Costa Toledano", "latitud": -34.6678, "longitud": -68.3456, 
             "detalles_referencia": "Costa Toledano - Zona Productiva"},
            {"ubicacion": "Colonia Iaccarini", "latitud": -34.6756, "longitud": -68.3567, 
             "detalles_referencia": "Colonia Iaccarini - Zona Rural"},
            {"ubicacion": "Montoya", "latitud": -34.6445, "longitud": -68.2334, 
             "detalles_referencia": "Montoya - Distrito Rural Este"},
            {"ubicacion": "El Cristo", "latitud": -34.6567, "longitud": -68.2456, 
             "detalles_referencia": "El Cristo - Zona Rural Este"},
            {"ubicacion": "Cuarteles", "latitud": -34.6889, "longitud": -68.3789, 
             "detalles_referencia": "Cuarteles - Acceso a Cañada Seca"}
        ]
        
        self.datos_completos["paradas"] = paradas_data
        
    def generar_lineas(self):
        """Genera las líneas de transporte con datos realistas"""
        lineas_data = [
            # EMPRESA ISELIN S.R.L.
            {"codigo": "511A", "nombre": "Río Diamante - Centro (por Sarmiento)", "empresa": "Iselin S.R.L.", "frecuencia": 30},
            {"codigo": "511B", "nombre": "Rama Caída - Centro (por Salas)", "empresa": "Iselin S.R.L.", "frecuencia": 35},
            {"codigo": "511C", "nombre": "Los Filtros - Terminal", "empresa": "Iselin S.R.L.", "frecuencia": 40},
            {"codigo": "512A", "nombre": "Barrio Cristiano - Barrio Unión Obrera", "empresa": "Iselin S.R.L.", "frecuencia": 45},
            {"codigo": "512B", "nombre": "Barrio Cristiano - El Cerrito", "empresa": "Iselin S.R.L.", "frecuencia": 50},
            {"codigo": "513A", "nombre": "Barrio UNIMEV - Cementerio (por Córdoba)", "empresa": "Iselin S.R.L.", "frecuencia": 40},
            {"codigo": "513B", "nombre": "Barrio Libertad - Cementerio (por Moreno)", "empresa": "Iselin S.R.L.", "frecuencia": 45},
            {"codigo": "514A", "nombre": "Valle Grande/Docente - Cementerio", "empresa": "Iselin S.R.L.", "frecuencia": 35},
            {"codigo": "514B", "nombre": "Valle Grande/Docente - Centro/Molino", "empresa": "Iselin S.R.L.", "frecuencia": 35},
            # EMPRESA A. BUTTINI E HIJOS S.R.L.
            {"codigo": "541", "nombre": "Zanjón Civit", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 60},
            {"codigo": "542", "nombre": "Cuadro Benegas - Pedro Vargas", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 45},
            {"codigo": "543", "nombre": "Pedro Vargas - Los Coroneles", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 50},
            {"codigo": "544", "nombre": "Salto de las Rosas - Bella Vista - Claveles", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 55},
            {"codigo": "547", "nombre": "El Nihuil", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 90},
            {"codigo": "548", "nombre": "Cañada Seca por Cuarteles", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 70},
            {"codigo": "571", "nombre": "Jensen por Dean Funes", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 60},
            {"codigo": "572", "nombre": "El Usillal", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 80},
            {"codigo": "573", "nombre": "Costa Toledano - Colonia Iaccarini", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 75},
            {"codigo": "574", "nombre": "Las Paredes - Montoya - El Cristo", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 65},
            {"codigo": "575", "nombre": "Villa 25 de Mayo", "empresa": "A. Buttini e Hijos S.R.L.", "frecuencia": 55}
        ]
        
        self.datos_completos["lineas"] = lineas_data
        
    def generar_recorridos_y_linea_paradas(self):
        """Genera los recorridos detallados y las relaciones línea-parada"""
        
        recorridos = {
            # LÍNEAS ISELIN
            "511A": ["Terminal San Rafael", "Plaza San Martín", "Banco Nación", "Centro Cívico", 
                     "Puente Río Diamante", "Río Diamante", "Cuadro Nacional"],
            "511B": ["Terminal San Rafael", "Plaza San Martín", "Municipalidad", "Hospital Schestakow", 
                     "Acceso Norte", "Rama Caída"],
            "511C": ["Los Filtros", "Acceso Norte", "Universidad Nacional", "Barrio Valle Grande", 
                     "Hospital Schestakow", "Plaza San Martín", "Terminal San Rafael"],
            "512A": ["Barrio Cristiano", "Barrio Libertad", "Plaza San Martín", "Centro Cívico", 
                     "Supermercado Libertad", "Barrio Unión Obrera"],
            "512B": ["Barrio Cristiano", "Plaza San Martín", "Municipalidad", "Acceso Sur Ruta 143", "El Cerrito"],
            "513A": ["Barrio UNIMEV", "Universidad Nacional", "Hospital Schestakow", "Centro Cívico", 
                     "Plaza San Martín", "Cementerio Municipal"],
            "513B": ["Barrio Libertad", "Plaza San Martín", "Municipalidad", "Hospital Schestakow", 
                     "Cementerio Municipal"],
            "514A": ["Barrio Valle Grande", "Barrio Docente", "Universidad Nacional", "Hospital Schestakow", 
                     "Centro Cívico", "Cementerio Municipal"],
            "514B": ["Barrio Valle Grande", "Barrio Docente", "Universidad Nacional", "Hospital Schestakow", 
                     "Plaza San Martín", "Terminal San Rafael"],
            # LÍNEAS A. BUTTINI
            "541": ["Terminal San Rafael", "Plaza San Martín", "Municipalidad", "Villa 25 de Mayo", "Zanjón Civit"],
            "542": ["Terminal San Rafael", "Plaza San Martín", "Villa 25 de Mayo", "Cuadro Benegas", "Pedro Vargas"],
            "543": ["Terminal San Rafael", "Plaza San Martín", "Pedro Vargas", "Los Coroneles"],
            "544": ["Terminal San Rafael", "Plaza San Martín", "Villa 25 de Mayo", "Bella Vista", 
                    "Claveles", "Salto de las Rosas"],
            "547": ["Terminal San Rafael", "Plaza San Martín", "Municipalidad", "Villa 25 de Mayo", 
                    "Zanjón Civit", "El Nihuil"],
            "548": ["Terminal San Rafael", "Plaza San Martín", "Barrio Unión Obrera", "Cuarteles", "Cañada Seca"],
            "571": ["Terminal San Rafael", "Plaza San Martín", "Universidad Nacional", "Los Filtros", "Jensen"],
            "572": ["Terminal San Rafael", "Plaza San Martín", "Los Filtros", "Acceso Norte", "El Usillal"],
            "573": ["Terminal San Rafael", "Plaza San Martín", "Barrio Unión Obrera", "Costa Toledano", "Colonia Iaccarini"],
            "574": ["Terminal San Rafael", "Plaza San Martín", "Cuadro Nacional", "Las Paredes", "Montoya", "El Cristo"],
            "575": ["Terminal San Rafael", "Plaza San Martín", "Centro Cívico", "Supermercado Libertad", "Villa 25 de Mayo"]
        }
        
        linea_paradas = []
        linea_parada_id = 1
        
        for codigo_linea, paradas_recorrido in recorridos.items():
            for orden, ubicacion_parada in enumerate(paradas_recorrido, 1):
                linea_paradas.append({
                    "id": linea_parada_id,
                    "linea_codigo": codigo_linea,
                    "parada_ubicacion": ubicacion_parada,
                    "orden": orden
                })
                linea_parada_id += 1
                
        self.datos_completos["linea_paradas"] = linea_paradas
        
    def generar_horarios_realistas(self):
        """Genera horarios realistas según el tipo de línea, asignados a la primera parada de cada línea"""
        horarios = []
        horario_id = 1
        
        horarios_urbanos = {
            "Habil": ["06:00", "06:30", "07:00", "07:30", "08:00", "08:30", "09:00", "09:30", 
                      "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
                      "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30",
                      "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00"],
            "Sabado": ["07:00", "07:45", "08:30", "09:15", "10:00", "10:45", "11:30", "12:15",
                       "13:00", "13:45", "14:30", "15:15", "16:00", "16:45", "17:30", "18:15",
                       "19:00", "19:45", "20:30"],
            "Domingo": ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00",
                        "16:00", "17:00", "18:00", "19:00", "20:00"]
        }
        
        horarios_suburbanos = {
            "Habil": ["06:30", "07:30", "08:30", "09:30", "10:30", "11:30", "12:30", "13:30",
                      "14:30", "15:30", "16:30", "17:30", "18:30", "19:30", "20:30"],
            "Sabado": ["07:30", "09:00", "10:30", "12:00", "13:30", "15:00", "16:30", "18:00", "19:30"],
            "Domingo": ["08:30", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
        }
        
        horarios_rurales = {
            "Habil": ["07:00", "09:00", "11:00", "13:00", "15:00", "17:00", "19:00"],
            "Sabado": ["08:00", "10:30", "13:00", "15:30", "18:00"],
            "Domingo": ["09:00", "12:00", "16:00", "19:00"]
        }
        
        lineas_urbanas = ["511A", "511B", "511C", "513A", "514A", "514B"]
        lineas_suburbanas = ["512A", "512B", "513B", "541", "542", "543", "575"]
        lineas_rurales = ["544", "547", "548", "571", "572", "573", "574"]
        
        for linea in self.datos_completos["lineas"]:
            codigo = linea["codigo"]
            # Encontrar la primera parada de la línea (orden=1)
            linea_parada = next((lp for lp in self.datos_completos["linea_paradas"] 
                                 if lp["linea_codigo"] == codigo and lp["orden"] == 1), None)
            if not linea_parada:
                continue  # Saltar si no hay paradas para la línea
                
            horarios_tipo = horarios_urbanos if codigo in lineas_urbanas else \
                           horarios_suburbanos if codigo in lineas_suburbanas else horarios_rurales
                
            for tipo_dia, horarios_dia in horarios_tipo.items():
                for hora_str in horarios_dia:
                    horarios.append({
                        "id": horario_id,
                        "linea_parada_id": linea_parada["id"],
                        "hora": hora_str,
                        "tipo_dia": tipo_dia
                    })
                    horario_id += 1
                    
        self.datos_completos["horarios"] = horarios
        
    def generar_rutas_larga_distancia(self):
        """Genera rutas de larga distancia para completar el sistema"""
        rutas = [
            {"id": 1, "origen": "San Rafael", "destino": "Mendoza"},
            {"id": 2, "origen": "San Rafael", "destino": "General Alvear"},
            {"id": 3, "origen": "San Rafael", "destino": "Malargüe"},
            {"id": 4, "origen": "San Rafael", "destino": "San Carlos"},
            {"id": 5, "origen": "San Rafael", "destino": "Tunuyán"},
            {"id": 6, "origen": "Mendoza", "destino": "San Rafael"},
            {"id": 7, "origen": "General Alvear", "destino": "San Rafael"},
            {"id": 8, "origen": "Malargüe", "destino": "San Rafael"}
        ]
        
        self.datos_completos["rutas"] = rutas
        
    def generar_viajes_ejemplo(self):
        """Genera algunos viajes de ejemplo para larga distancia"""
        viajes = [
            {"id": 1, "ruta_id": 1, "empresa": "Iselin S.R.L.", "hora_salida": "07:00", "hora_llegada": "09:30", "costo_base": 2500.0},
            {"id": 2, "ruta_id": 1, "empresa": "Iselin S.R.L.", "hora_salida": "14:00", "hora_llegada": "16:30", "costo_base": 2500.0},
            {"id": 3, "ruta_id": 1, "empresa": "A. Buttini e Hijos S.R.L.", "hora_salida": "10:30", "hora_llegada": "13:00", "costo_base": 2600.0},
            {"id": 4, "ruta_id": 2, "empresa": "A. Buttini e Hijos S.R.L.", "hora_salida": "08:00", "hora_llegada": "09:15", "costo_base": 1800.0},
            {"id": 5, "ruta_id": 3, "empresa": "Iselin S.R.L.", "hora_salida": "06:30", "hora_llegada": "10:00", "costo_base": 3200.0},
            {"id": 6, "ruta_id": 6, "empresa": "Iselin S.R.L.", "hora_salida": "17:00", "hora_llegada": "19:30", "costo_base": 2500.0},
            {"id": 7, "ruta_id": 7, "empresa": "A. Buttini e Hijos S.R.L.", "hora_salida": "16:30", "hora_llegada": "17:45", "costo_base": 1800.0}
        ]
        
        self.datos_completos["viajes"] = viajes
        
    def generar_todos_los_datos(self):
        """Genera todos los datos del sistema"""
        print("🚌 Generando datos completos para transporte San Rafael...")
        
        self.generar_empresas()
        print("✅ Empresas generadas")
        
        self.generar_paradas()
        print("✅ Paradas generadas")
        
        self.generar_lineas()
        print("✅ Líneas generadas")
        
        self.generar_recorridos_y_linea_paradas()
        print("✅ Recorridos y relaciones línea-parada generadas")
        
        self.generar_horarios_realistas()
        print("✅ Horarios realistas generados")
        
        self.generar_rutas_larga_distancia()
        print("✅ Rutas de larga distancia generadas")
        
        self.generar_viajes_ejemplo()
        print("✅ Viajes de ejemplo generados")
        
        self.datos_completos["metadata"] = {
            "fecha_generacion": datetime.now().isoformat(),
            "version": "1.0",
            "descripcion": "Datos completos del sistema de transporte de San Rafael",
            "total_registros": {
                "empresas": len(self.datos_completos["empresas"]),
                "paradas": len(self.datos_completos["paradas"]),
                "lineas": len(self.datos_completos["lineas"]),
                "linea_paradas": len(self.datos_completos["linea_paradas"]),
                "horarios": len(self.datos_completos["horarios"]),
                "rutas": len(self.datos_completos["rutas"]),
                "viajes": len(self.datos_completos["viajes"])
            }
        }
        
        return self.datos_completos
        
    def guardar_json(self, archivo_salida="datos_transporte_completo.json"):
        """Guarda los datos en un archivo JSON"""
        ruta_archivo = os.path.join(os.path.dirname(__file__), archivo_salida)
        
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(self.datos_completos, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Datos guardados en: {ruta_archivo}")
        return ruta_archivo
        
    def mostrar_estadisticas(self):
        """Muestra estadísticas de los datos generados"""
        metadata = self.datos_completos["metadata"]
        
        print("\n📊 ESTADÍSTICAS DE DATOS GENERADOS:")
        print(f"   🏢 Empresas: {metadata['total_registros']['empresas']}")
        print(f"   🚏 Paradas: {metadata['total_registros']['paradas']}")
        print(f"   🚌 Líneas: {metadata['total_registros']['lineas']}")
        print(f"   🛤️ Relaciones Línea-Parada: {metadata['total_registros']['linea_paradas']}")
        print(f"   ⏰ Horarios: {metadata['total_registros']['horarios']}")
        print(f"   🛣️ Rutas Larga Distancia: {metadata['total_registros']['rutas']}")
        print(f"   🚍 Viajes: {metadata['total_registros']['viajes']}")
        
        print("\n🏢 DETALLE POR EMPRESA:")
        for empresa in self.datos_completos["empresas"]:
            lineas_empresa = [l for l in self.datos_completos["lineas"] if l["empresa"] == empresa["nombre"]]
            print(f"   • {empresa['nombre']}: {len(lineas_empresa)} líneas")

if __name__ == "__main__":
    # Crear una instancia de la clase
    generador = GeneradorDatosTransporte()
    
    # Generar todos los datos
    datos = generador.generar_todos_los_datos()
    
    # Guardar en JSON
    archivo_json = generador.guardar_json()
    
    # Mostrar estadísticas
    generador.mostrar_estadisticas()
    
    print(f"\n🎯 PRÓXIMO PASO: Ejecutar el script de carga a la base de datos")
    print(f"   python seeds/load_to_database.py")