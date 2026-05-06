## Context

Con las funcionalidades de creación, listado y edición completas, la eliminación es el último paso del CRUD de conceptos. Sin embargo, debido a la naturaleza recurrente de algunos gastos, un borrado ingenuo podría ser confuso o destructivo para el historial.

## Goals / Non-Goals

**Goals:**
- Implementar la eliminación de un concepto específico por ID.
- Diferenciar entre una eliminación total (cuando no hay historial) y una desactivación de recurrencia (cuando sí lo hay).
- Solicitar confirmación explícita al usuario antes de proceder.

**Non-Goals:**
- No se implementará "Deshacer" (Undo) en esta etapa; la confirmación previa es la salvaguarda.
- No se permitirá la eliminación masiva de conceptos en esta HU.

## Decisions

1. **QueryBuilder**:
   - Se debe añadir el método `delete()` a la clase `QueryBuilder` para soportar sentencias `DELETE`.

2. **Capa de Datos (`ConceptoRepository`)**:
   - `delete_concepto(id)`: Elimina el registro por su clave primaria.
   - `delete_plantilla_recurrente(nombre)`: Elimina la plantilla para que no se genere en meses futuros.
   - `count_history(nombre)`: Cuenta cuántos registros existen en la tabla `conceptos` con ese nombre.

3. **Capa de Servicio (`ConceptoService`)**:
   - `evaluar_tipo_eliminacion(nombre)`: Retorna si la eliminación será "Definitiva" (count == 1, el que se va a borrar) o "Desactivación de Recurrencia" (count > 1).
   - `eliminar_concepto(id, nombre, es_recurrente)`: 
     1. Borra el concepto (`delete_concepto`).
     2. Si era recurrente, borra la plantilla (`delete_plantilla_recurrente`). Esto detiene la recurrencia futura sin tocar el historial pasado (los registros en `conceptos` de meses anteriores permanecen intactos).

4. **Interfaz de Usuario (UI)**:
   - Se añadirá un botón "🗑️" en `ConceptListFrame` (columna Acción).
   - El botón disparará un `messagebox.askyesno` personalizado con la información proveída por el servicio sobre el tipo de eliminación.

## Risks / Trade-offs

- **Identificación por Nombre en Plantilla:** Al igual que en la edición, la eliminación de plantillas se basa en el nombre. Si existen dos conceptos distintos con el mismo nombre pero diferente comportamiento, ambos dejarían de ser recurrentes. Es un límite aceptado del esquema actual simplificado.
