import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from ..services.periodo_service import PeriodoService
from ..services.concepto_service import ConceptoService
from .components.period_list import PeriodListFrame
from .components.concepto_form import ConceptoForm
from .components.concept_list import ConceptListFrame

class App(ctk.CTk):
    def __init__(self, periodo_service: PeriodoService, concepto_service: ConceptoService):
        super().__init__()

        self.periodo_service = periodo_service
        self.concepto_service = concepto_service
        self.title("Finanzas Personales - Antigravity")
        self.geometry("900x600")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.setup_sidebar()
        self.setup_main_area()

        self.check_current_period()

    def setup_sidebar(self):
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(2, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Antigravity", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Etiqueta de sección de periodos
        self.period_section_label = ctk.CTkLabel(self.sidebar_frame, text="PERIODOS", font=ctk.CTkFont(size=12, weight="bold"))
        self.period_section_label.grid(row=1, column=0, padx=20, pady=(20, 5), sticky="w")

        # Integrar el componente de lista de periodos
        self.period_list = PeriodListFrame(self.sidebar_frame, self.periodo_service)
        self.period_list.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        
        self.refresh_period_list()

    def refresh_period_list(self):
        self.period_list.refresh()

    def setup_main_area(self):
        self.main_content = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_content.grid(row=0, column=1, sticky="nsew")

        self.welcome_label = ctk.CTkLabel(self.main_content, text="Bienvenido a tu Dashboard", font=ctk.CTkFont(size=16))
        self.welcome_label.pack(pady=20)

        self.add_btn = ctk.CTkButton(self.main_content, text="➕ Agregar Concepto", command=self.open_add_concepto)
        self.add_btn.pack(pady=10)

        # Instanciar tabla de conceptos
        self.concept_list = ConceptListFrame(self.main_content, self.concepto_service)
        self.concept_list.pack(fill="both", expand=True, padx=20, pady=20)

    def open_add_concepto(self):
        now = datetime.now()
        ConceptoForm(self, self.concepto_service, now.month, now.year, on_success=self.refresh_dashboard)

    def refresh_dashboard(self):
        self.refresh_period_list()
        now = datetime.now()
        self.concept_list.set_periodo(now.month, now.year)

    def check_current_period(self):
        now = datetime.now()
        mes, anio = now.month, now.year
        
        # Establecer el periodo actual en la tabla
        self.concept_list.set_periodo(mes, anio)

        if not self.periodo_service.verificar_existencia(mes, anio):
            respuesta = messagebox.askyesno(
                "Nuevo Periodo",
                f"El periodo {mes}/{anio} no existe.\n¿Desea crearlo ahora?"
            )
            
            if respuesta:
                try:
                    self.periodo_service.crear_periodo(mes, anio)
                    messagebox.showinfo("Éxito", "Periodo creado correctamente.")
                    self.refresh_dashboard()
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo crear el periodo: {e}")
            else:
                messagebox.showwarning("Aviso", "No se ha creado el periodo. Algunas funcionalidades podrían estar limitadas.")

if __name__ == "__main__":
    # Esto es solo para testing rápido si se ejecuta el archivo directamente
    pass
