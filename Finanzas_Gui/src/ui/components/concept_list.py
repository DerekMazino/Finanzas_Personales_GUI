import customtkinter as ctk
from tkinter import messagebox

class ConceptListFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, concepto_service, **kwargs):
        super().__init__(master, **kwargs)
        self.concepto_service = concepto_service
        self.mes_actual = None
        self.anio_actual = None

    def set_periodo(self, mes, anio):
        self.mes_actual = mes
        self.anio_actual = anio
        self.refresh()

    def refresh(self):
        # Limpiar widgets existentes
        for widget in self.winfo_children():
            widget.destroy()

        if not self.mes_actual or not self.anio_actual:
            return

        conceptos = self.concepto_service.obtener_conceptos_por_periodo(self.mes_actual, self.anio_actual)

        # Estado vacío
        if not conceptos:
            ctk.CTkLabel(self, text="No hay conceptos registrados para este periodo. ¡Comienza agregando uno!", 
                         font=ctk.CTkFont(size=14, slant="italic")).pack(pady=50)
            return

        # Encabezados
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        headers = ["Nombre", "Valor", "Tipo", "Recurrente", "Acción"]
        for i, header in enumerate(headers):
            lbl = ctk.CTkLabel(header_frame, text=header, font=ctk.CTkFont(weight="bold"))
            lbl.grid(row=0, column=i, sticky="w", padx=20)
            header_frame.grid_columnconfigure(i, weight=1)

        # Filas
        for row, concepto in enumerate(conceptos, start=1):
            # concepto puede tener más de 6 campos (ej. created_at), así que usamos *_ al final
            _, _, nombre, valor, tipo, es_recurrente, *_ = concepto
            
            row_frame = ctk.CTkFrame(self)
            row_frame.pack(fill="x", padx=10, pady=2)
            
            # Nombre
            ctk.CTkLabel(row_frame, text=nombre).grid(row=0, column=0, sticky="w", padx=20, pady=5)
            # Valor
            ctk.CTkLabel(row_frame, text=f"${valor:.2f}", text_color="#2ecc71" if tipo == "ingreso" else "#e74c3c").grid(row=0, column=1, sticky="w", padx=20, pady=5)
            # Tipo
            ctk.CTkLabel(row_frame, text=tipo.capitalize()).grid(row=0, column=2, sticky="w", padx=20, pady=5)
            # Recurrente
            ctk.CTkLabel(row_frame, text="Sí" if es_recurrente else "No").grid(row=0, column=3, sticky="w", padx=20, pady=5)
            
            # Botones de Acción
            actions_frame = ctk.CTkFrame(row_frame, fg_color="transparent")
            actions_frame.grid(row=0, column=4, padx=20, pady=5)
            
            edit_btn = ctk.CTkButton(actions_frame, text="✏️", width=30, command=lambda c=concepto: self.open_edit_form(c))
            edit_btn.pack(side="left", padx=2)
            
            delete_btn = ctk.CTkButton(actions_frame, text="🗑️", width=30, fg_color="#c0392b", hover_color="#962d22",
                                      command=lambda c=concepto: self.confirmar_eliminacion(c))
            delete_btn.pack(side="left", padx=2)

            for i in range(5):
                row_frame.grid_columnconfigure(i, weight=1)

    def open_edit_form(self, concepto):
        from .concepto_form import ConceptoForm
        # Se abre ConceptoForm en la ventana principal, pasándole los datos del concepto para edición
        ConceptoForm(self.winfo_toplevel(), self.concepto_service, self.mes_actual, self.anio_actual, 
                     on_success=self.refresh, concepto_existente=concepto)

    def confirmar_eliminacion(self, concepto):
        id_c, _, nombre, _, _, es_recurrente, *_ = concepto
        
        titulo, mensaje = self.concepto_service.obtener_info_eliminacion(nombre)
        
        if messagebox.askyesno(f"Confirmar: {titulo}", f"{mensaje}\n\n¿Estás seguro de que deseas eliminar '{nombre}'?"):
            self.concepto_service.eliminar_concepto(id_c, nombre, es_recurrente)
            self.refresh()
