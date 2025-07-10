from app.models.paradas import Parada
from app.models.linea_parada import LineaParada
from app.models.linea import Linea
from app.models.empresa import Empresa
from app.models.horario import Horario
from app import db
from datetime import datetime, time
from sqlalchemy import and_

class ParadaService:
    
    @staticmethod
    def obtener_todas_paradas():
        """Obtiene todas las paradas para mostrar en el mapa"""
        return Parada.query.all()
    
    @staticmethod
    def obtener_parada_por_id(parada_id):
        """Obtiene una parada específica por ID"""
        return Parada.query.get(parada_id)
    
    @staticmethod
    def obtener_lineas_por_parada(parada_id):
        """Obtiene todas las líneas que pasan por una parada específica"""
        return db.session.query(Linea, Empresa, LineaParada.orden)\
            .join(LineaParada, Linea.id == LineaParada.linea_id)\
            .join(Empresa, Linea.empresa_id == Empresa.id)\
            .filter(LineaParada.parada_id == parada_id)\
            .order_by(Linea.codigo)\
            .all()
    
    @staticmethod
    def obtener_horarios_por_parada(parada_id, tipo_dia=None):
        """Obtiene los horarios de todas las líneas que pasan por una parada"""
        if tipo_dia is None:
            # Determinar el tipo de día actual
            hoy = datetime.now().weekday()
            if hoy == 5:  # Sábado
                tipo_dia = 'Sabado'
            elif hoy == 6:  # Domingo
                tipo_dia = 'Domingo'
            else:  # Lunes a Viernes
                tipo_dia = 'Habil'
        
        return db.session.query(Horario, Linea, Empresa)\
            .join(LineaParada, Horario.linea_parada == LineaParada.id)\
            .join(Linea, LineaParada.linea_id == Linea.id)\
            .join(Empresa, Linea.empresa_id == Empresa.id)\
            .filter(and_(
                LineaParada.parada_id == parada_id,
                Horario.tipo_dia == tipo_dia
            ))\
            .order_by(Linea.codigo, Horario.hora)\
            .all()
    
    @staticmethod
    def calcular_proxima_llegada(horarios):
        """Calcula el tiempo hasta la próxima llegada para cada línea"""
        hora_actual = datetime.now().time()
        resultado = []
        
        for horario, linea, empresa in horarios:
            if horario.hora > hora_actual:
                # Calcular diferencia en minutos
                delta = datetime.combine(datetime.today(), horario.hora) - \
                       datetime.combine(datetime.today(), hora_actual)
                minutos = int(delta.total_seconds() / 60)
                proxima_llegada = f"{minutos} minutos"
            else:
                proxima_llegada = "Próximo horario mañana"
            
            resultado.append({
                'horario': horario,
                'linea': linea,
                'empresa': empresa,
                'proxima_llegada': proxima_llegada
            })
        
        return resultado
