from .connection import DBConnection
from .query_builder import QueryBuilder

class ConceptoRepository:
    def __init__(self, db: DBConnection):
        self.db = db
        self.table = "conceptos"

    def create(self, periodo_id, nombre, valor, tipo, es_recurrente=0):
        data = {
            "periodo_id": periodo_id,
            "nombre": nombre,
            "valor": valor,
            "tipo": tipo,
            "es_recurrente": es_recurrente
        }
        query, params = QueryBuilder(self.table).insert(data).build()
        self.db.execute_query(query, params)

    def get_by_periodo(self, periodo_id):
        query, params = QueryBuilder(self.table).select().where("periodo_id", periodo_id).build()
        return self.db.fetch_all(query, params)

    def get_recurrentes_last_period(self, periodo_id):
        # Esta lógica se refinará en el servicio, pero el repo provee el acceso
        query, params = QueryBuilder(self.table).select().where("es_recurrente", 1).where("periodo_id", periodo_id).build()
        return self.db.fetch_all(query, params)

    def update_concepto(self, id, nombre, valor, tipo, es_recurrente):
        data = {
            "nombre": nombre,
            "valor": valor,
            "tipo": tipo,
            "es_recurrente": es_recurrente
        }
        query, params = QueryBuilder(self.table).update(data).where("id", id).build()
        self.db.execute_query(query, params)

    def update_plantilla_name(self, old_nombre, new_nombre):
        query, params = QueryBuilder("plantillas_recurrentes").update({"nombre": new_nombre}).where("nombre", old_nombre).build()
        self.db.execute_query(query, params)

    def delete_concepto(self, id):
        query, params = QueryBuilder(self.table).delete().where("id", id).build()
        self.db.execute_query(query, params)

    def delete_plantilla_recurrente(self, nombre):
        query, params = QueryBuilder("plantillas_recurrentes").delete().where("nombre", nombre).build()
        self.db.execute_query(query, params)

    def count_history(self, nombre):
        query, params = QueryBuilder(self.table).select("COUNT(*)").where("nombre", nombre).build()
        result = self.db.fetch_one(query, params)
        return result[0] if result else 0
