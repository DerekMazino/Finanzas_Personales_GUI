from .connection import DBConnection
from .query_builder import QueryBuilder

class PeriodoRepository:
    def __init__(self, db: DBConnection):
        self.db = db
        self.table = "periodos"

    def create(self, mes, anio):
        query, params = QueryBuilder(self.table).insert({"mes": mes, "anio": anio}).build()
        self.db.execute_query(query, params)

    def get_by_date(self, mes, anio):
        query, params = QueryBuilder(self.table).select().where("mes", mes).where("anio", anio).build()
        result = self.db.fetch_all(query, params)
        return result[0] if result else None

    def get_all(self):
        query, params = QueryBuilder(self.table).select().build()
        return self.db.fetch_all(query, params)
