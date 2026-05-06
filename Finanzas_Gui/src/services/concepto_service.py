import re
from .periodo_service import PeriodoService
from ..database.concepto_repository import ConceptoRepository

class ConceptoService:
    def __init__(self, concepto_repo: ConceptoRepository, periodo_service: PeriodoService):
        self.concepto_repo = concepto_repo
        self.periodo_service = periodo_service

    def validar_datos(self, nombre, valor, tipo):
        if not nombre or not re.match(r'^[a-zA-Z]', nombre):
            raise ValueError("El nombre debe comenzar con una letra del alfabeto.")
        
        try:
            val = float(valor)
        except (ValueError, TypeError):
            raise ValueError("El valor debe ser un número válido.")
            
        if val <= 0:
            raise ValueError("El valor debe ser un número positivo.")
            
        if tipo not in ['ingreso', 'egreso']:
            raise ValueError("El tipo debe ser 'ingreso' o 'egreso'.")

    def agregar_concepto(self, mes, anio, nombre, valor, tipo, es_recurrente=False):
        self.validar_datos(nombre, valor, tipo)

        # 2.2 Auto-crear periodo si no existe
        if not self.periodo_service.verificar_existencia(mes, anio):
            self.periodo_service.crear_periodo(mes, anio)
        
        # Obtener el ID del periodo
        periodo = self.periodo_service.periodo_repo.get_by_mes_anio(mes, anio)
        if not periodo:
            raise Exception(f"No se pudo encontrar ni crear el periodo {mes}/{anio}")
        
        periodo_id = periodo[0]

        # Guardar el concepto
        nuevo_id = self.concepto_repo.create(
            periodo_id=periodo_id,
            nombre=nombre,
            valor=float(valor),
            tipo=tipo,
            es_recurrente=1 if es_recurrente else 0
        )

        # 2.3 Si es recurrente, guardar en plantillas
        if es_recurrente:
            self.concepto_repo.db.execute_query(
                "INSERT INTO plantillas_recurrentes (nombre, valor, tipo) VALUES (?, ?, ?)",
                (nombre, float(valor), tipo)
            )
        
        return nuevo_id
