from .connection import DBConnection

class Migrator:
    def __init__(self, db_connection: DBConnection):
        self.db = db_connection

    def create_tables(self):
        # Tabla de Periodos
        self.db.execute_query("""
            CREATE TABLE IF NOT EXISTS periodos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mes INTEGER NOT NULL,
                anio INTEGER NOT NULL,
                UNIQUE(mes, anio)
            )
        """)

        # Tabla de Plantillas Recurrentes
        self.db.execute_query("""
            CREATE TABLE IF NOT EXISTS plantillas_recurrentes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                valor REAL NOT NULL,
                tipo TEXT NOT NULL CHECK(tipo IN ('ingreso', 'egreso'))
            )
        """)

        # Tabla de Conceptos (Transacciones)
        self.db.execute_query("""
            CREATE TABLE IF NOT EXISTS conceptos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                periodo_id INTEGER NOT NULL,
                nombre TEXT NOT NULL,
                valor REAL NOT NULL,
                tipo TEXT NOT NULL CHECK(tipo IN ('ingreso', 'egreso')),
                es_recurrente INTEGER DEFAULT 0,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (periodo_id) REFERENCES periodos(id)
            )
        """)
        print("Tablas creadas exitosamente.")

if __name__ == "__main__":
    db = DBConnection()
    migrator = Migrator(db)
    migrator.create_tables()
