import customtkinter as ctk
from tkinter import messagebox

class ConceptoForm(ctk.CTkToplevel):
    def __init__(self, master, concepto_service, mes_actual, anio_actual, on_success=None, concepto_existente=None):
        super().__init__(master)
        self.concepto_service = concepto_service
        self.mes_actual = mes_actual
        self.anio_actual = anio_actual
        self.on_success = on_success
        self.concepto_existente = concepto_existente
        
        self.title("Modificar Concepto" if concepto_existente else "Nuevo Concepto")
        self.geometry("400x500")
        self.setup_ui()
        
        # Enfocar ventana
        self.grab_set()

    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(self, text="AGREGAR CONCEPTO", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, pady=20)

        # Nombre
        ctk.CTkLabel(self, text="Nombre del concepto:").grid(row=1, column=0, padx=20, sticky="w")
        self.nombre_entry = ctk.CTkEntry(self, placeholder_text="Ej: Sueldo, Renta...")
        self.nombre_entry.grid(row=2, column=0, padx=20, pady=(0, 15), sticky="ew")

        # Valor
        ctk.CTkLabel(self, text="Valor:").grid(row=3, column=0, padx=20, sticky="w")
        self.valor_entry = ctk.CTkEntry(self, placeholder_text="0.00")
        self.valor_entry.grid(row=4, column=0, padx=20, pady=(0, 15), sticky="ew")

        # Tipo
        ctk.CTkLabel(self, text="Tipo:").grid(row=5, column=0, padx=20, sticky="w")
        self.tipo_var = ctk.StringVar(value="egreso")
        self.tipo_btn = ctk.CTkSegmentedButton(self, values=["ingreso", "egreso"], variable=self.tipo_var)
        self.tipo_btn.grid(row=6, column=0, padx=20, pady=(0, 15), sticky="ew")

        # Recurrente
        self.recurrente_var = ctk.BooleanVar(value=False)
        self.recurrente_switch = ctk.CTkSwitch(self, text="Es recurrente", variable=self.recurrente_var)
        self.recurrente_switch.grid(row=7, column=0, padx=20, pady=(0, 15), sticky="w")

        # Pre-llenado en modo edición
        if self.concepto_existente:
            _, _, nombre, valor, tipo, es_recurrente, *_ = self.concepto_existente
            self.nombre_entry.insert(0, nombre)
            self.valor_entry.insert(0, str(valor))
            self.tipo_var.set(tipo)
            self.recurrente_var.set(bool(es_recurrente))
            self.recurrente_switch.configure(state="disabled") # No permitir cambiar si es recurrente o no en modo edición


        # Botones
        self.save_btn = ctk.CTkButton(self, text="Guardar", command=self.save)
        self.save_btn.grid(row=8, column=0, padx=20, pady=20, sticky="ew")

    def save(self):
        nombre = self.nombre_entry.get()
        valor = self.valor_entry.get()
        tipo = self.tipo_var.get()
        es_recurrente = self.recurrente_var.get()

        try:
            if self.concepto_existente:
                id_conc = self.concepto_existente[0]
                old_nombre = self.concepto_existente[2]
                self.concepto_service.modificar_concepto(
                    id_conc, old_nombre, nombre, valor, tipo, es_recurrente
                )
                messagebox.showinfo("Éxito", "Concepto modificado correctamente.")
            else:
                self.concepto_service.agregar_concepto(
                    self.mes_actual, self.anio_actual,
                    nombre, valor, tipo, es_recurrente
                )
                messagebox.showinfo("Éxito", "Concepto guardado correctamente.")

            if self.on_success:
                self.on_success()
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
