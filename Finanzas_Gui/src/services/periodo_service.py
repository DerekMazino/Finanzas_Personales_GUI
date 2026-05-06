from ..database.periodo_repository import PeriodoRepository
from ..database.concepto_repository import ConceptoRepository

class PeriodoService:
    def __init__(self, periodo_repo: PeriodoRepository, concepto_repo: ConceptoRepository):
        self.periodo_repo = periodo_repo
        self.concepto_repo = concepto_repo

    def verificar_existencia(self, mes, anio):
        return self.periodo_repo.get_by_date(mes, anio) is not None

    def crear_periodo(self, mes, anio):
        if self.verificar_existencia(mes, anio):
            raise ValueError(f"El periodo {mes}/{anio} ya existe.")
        
        self.periodo_repo.create(mes, anio)
        nuevo_periodo = self.periodo_repo.get_by_date(mes, anio)
        
        # Lógica de copia de recurrentes (HU-1 Criterio 1.1)
        self._copiar_conceptos_recurrentes(nuevo_periodo[0])
        return nuevo_periodo

    def _copiar_conceptos_recurrentes(self, nuevo_periodo_id):
        # Buscamos todos los periodos anteriores para encontrar el último con recurrentes
        # Por simplicidad en este MVP, buscamos en todos los conceptos marcados como recurrentes
        # En una versión más avanzada, filtraríamos por el último periodo cronológico.
        periodos = self.periodo_repo.get_all()
        if len(periodos) <= 1:
            return # No hay periodos anteriores
        
        # Ordenamos por año y mes descendentemente para obtener el anterior más reciente
        # periodos: list of tuples (id, mes, anio)
        periodos_sorted = sorted(periodos, key=lambda x: (x[2], x[1]), reverse=True)
        
        # El primer elemento es el nuevo periodo, el segundo es el anterior
        ultimo_periodo_id = periodos_sorted[1][0]
        
        conceptos_recurrentes = self.concepto_repo.get_recurrentes_last_period(ultimo_periodo_id)
        
        for concepto in conceptos_recurrentes:
            # concepto: (id, periodo_id, nombre, valor, tipo, es_recurrente, fecha)
            self.concepto_repo.create(
                periodo_id=nuevo_periodo_id,
                nombre=concepto[2],
                valor=concepto[3],
                tipo=concepto[4],
                es_recurrente=1
            )

    def obtener_todos_formateados(self):
        """Devuelve una lista de diccionarios con mes_nombre, anio e id, ordenados desc."""
        periodos = self.periodo_repo.get_all()
        # periodos: list of tuples (id, mes, anio)
        
        # Mapeo de meses en español
        nombres_meses = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
            5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
            9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }

        # Ordenar: año descendente, mes descendente
        periodos_sorted = sorted(periodos, key=lambda x: (x[2], x[1]), reverse=True)

        return [
            {
                "id": p[0],
                "mes_nombre": nombres_meses.get(p[1], "Desconocido"),
                "anio": p[2]
            }
            for p in periodos_sorted
        ]
