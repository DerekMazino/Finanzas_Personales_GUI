from src.database.connection import DBConnection
from src.database.periodo_repository import PeriodoRepository
from src.database.concepto_repository import ConceptoRepository
from src.services.periodo_service import PeriodoService
from src.ui.app import App
import customtkinter as ctk

def main():
    # Inicialización de dependencias
    db = DBConnection()
    periodo_repo = PeriodoRepository(db)
    concepto_repo = ConceptoRepository(db)
    periodo_service = PeriodoService(periodo_repo, concepto_repo)

    # Configuración de apariencia
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Inicio de la aplicación
    app = App(periodo_service)
    app.mainloop()

if __name__ == "__main__":
    main()
