import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from ..services.periodo_service import PeriodoService
from .components.period_list import PeriodListFrame

class App(ctk.CTk):
    def __init__(self, periodo_service: PeriodoService):
        super().__init__()

        self.periodo_service = periodo_service
        self.title("Finanzas Personales - Antigravity")
        self.geometry("900x600")

        self.setup_ui()
        self.check_current_period()

    def setup_ui(self):
        # Layout básico del Dashboard
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.title_label = ctk.CTkLabel(self.sidebar, text="FINANZAS", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(padx=20, pady=20)

        # Sección de Periodos en Sidebar
        self.period_label = ctk.CTkLabel(self.sidebar, text="PERIODOS", font=ctk.CTkFont(size=14, weight="bold"))
        self.period_label.pack(pady=(10, 5))

        self.refresh_period_list()

        self.main_content = ctk.CTkFrame(self, corner_radius=10)
        self.main_content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    def refresh_period_list(self):
        periodos = self.periodo_service.obtener_todos_formateados()
        if hasattr(self, 'period_list_frame'):
            self.period_list_frame.destroy()
        
        self.period_list_frame = PeriodListFrame(self.sidebar, periodos, width=200, height=300)
        self.period_list_frame.pack(padx=10, pady=10, fill="both", expand=True)

    def check_current_period(self):
        now = datetime.now()
        mes, anio = now.month, now.year

        if not self.periodo_service.verificar_existencia(mes, anio):
            self.prompt_create_period(mes, anio)
        else:
            self.refresh_period_list()

        self.welcome_label = ctk.CTkLabel(self.main_content, text="Bienvenido a tu Dashboard", font=ctk.CTkFont(size=16))
        self.welcome_label.pack(pady=20)

    def check_current_period(self):
        now = datetime.now()
        mes, anio = now.month, now.year

        if not self.periodo_service.verificar_existencia(mes, anio):
            self.prompt_create_period(mes, anio)

    def prompt_create_period(self, mes, anio):
        # RULE-02: No se permite código sin una HU previa. Esta UI cumple con F1 HU1.
        mensaje = f"El periodo {mes}/{anio} no existe. ¿Desea crearlo ahora?\nSe copiarán los conceptos recurrentes del mes anterior."
        
        if messagebox.askyesno("Nuevo Periodo", mensaje):
            try:
                self.periodo_service.crear_periodo(mes, anio)
                messagebox.showinfo("Éxito", f"Periodo {mes}/{anio} creado exitosamente.")
                self.refresh_period_list()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Aviso", "No se ha creado el periodo. Algunas funcionalidades podrían estar limitadas.")

if __name__ == "__main__":
    # Esto es solo para testing rápido si se ejecuta el archivo directamente
    pass
