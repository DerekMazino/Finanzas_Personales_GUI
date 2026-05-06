## Context

Actualmente el sistema permite agregar conceptos (normales o recurrentes) y listarlos por periodo. Para completar el ciclo de vida de la información, el usuario requiere poder modificar estos datos si cometió un error o si el valor/tipo de una transacción ha cambiado en un mes particular.

## Goals / Non-Goals

**Goals:**
- Permitir la modificación de un concepto financiero registrado.
- Validar los datos de entrada al modificar (igual que al crear).
- Manejar correctamente la lógica de propagación de cambios de nombre para conceptos recurrentes (actualizando la plantilla global).

**Non-Goals:**
- No se busca poder cambiar el estado "recurrente" de un concepto ya creado (activar/desactivar la recurrencia no está especificado en esta historia).
- No se deben alterar los nombres de los conceptos en periodos pasados.

## Decisions

1. **Persistencia (`ConceptoRepository`)**:
   - Crear un nuevo método `update_concepto(id, nombre, valor, tipo)`.
   - Crear un método para modificar el nombre en la plantilla: `update_plantilla_name(old_nombre, new_nombre)`. Dado que `plantillas_recurrentes` usa el nombre como llave conceptual (o al menos no tenemos en el código un ID mapeado a nivel de UI para la plantilla), la actualización se hará basada en el `old_nombre`.

2. **Lógica de Negocio (`ConceptoService`)**:
   - Crear `modificar_concepto(id, old_nombre, new_nombre, valor, tipo, es_recurrente)`.
   - Realizará las validaciones estándar (reutilizando `validar_datos`).
   - Si `es_recurrente` es verdadero y `old_nombre != new_nombre`, llamará a `update_plantilla_name`.
   - Finalmente, llamará a `update_concepto`.

3. **Interfaz de Usuario (UI)**:
   - Se modificará `ConceptListFrame` para agregar un botón "✏️" (Editar) en cada fila de concepto.
   - Al presionar el botón, se abrirá el componente existente `ConceptoForm`.
   - Se refactorizará `ConceptoForm` para que pueda recibir opcionalmente un `concepto_existente` por constructor. Si lo recibe, el formulario entrará en "Modo Edición" pre-llenando los campos y al guardar, ejecutará `modificar_concepto` en lugar de agregar.

## Risks / Trade-offs

- **Identificador de la plantilla:** Si el usuario tiene dos plantillas recurrentes que se llaman exactamente igual (ej. "Suscripción"), actualizar por nombre (`WHERE nombre = old_nombre`) actualizaría ambas. Dado el contexto simplificado de SQLite actual, es un trade-off aceptable, aunque a futuro las plantillas deberían estar vinculadas por una foreign key directa si se requiere alta precisión.
