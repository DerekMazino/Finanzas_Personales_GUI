import customtkinter as ctk

class PeriodListFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, periodo_service, **kwargs):
        super().__init__(master, **kwargs)
        self.periodo_service = periodo_service
        self.setup_ui()

    def refresh(self):
        self.setup_ui()

    def setup_ui(self):
        # Limpiar frame si tuviera algo
        for child in self.winfo_children():
            child.destroy()

        periodos = self.periodo_service.obtener_todos_formateados()

        if not periodos:
            self.empty_label = ctk.CTkLabel(self, text="No hay periodos registrados.\n¡Crea el primero!", font=ctk.CTkFont(size=14, slant="italic"))
            self.empty_label.pack(pady=40)
            return

        for p in periodos:
            text = f"{p['mes_nombre']} {p['anio']}"
            btn = ctk.CTkButton(self, text=text, fg_color="transparent", border_width=1, anchor="w")
            btn.pack(fill="x", pady=2, padx=5)
