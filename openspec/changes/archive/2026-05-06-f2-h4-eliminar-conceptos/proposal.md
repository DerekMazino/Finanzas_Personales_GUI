## Why

Los usuarios necesitan poder eliminar registros que fueron ingresados por error. Sin embargo, en un sistema de finanzas con conceptos recurrentes, una eliminación simple podría afectar el historial pasado o dejar huérfanos registros futuros. Este cambio introduce una eliminación "inteligente" que distingue entre corregir un error puntual y dar de baja un gasto recurrente preservando su historia.

## What Changes

- Nueva funcionalidad de eliminación accesible desde la lista de conceptos.
- Diálogo de confirmación que informa al usuario sobre el tipo de eliminación (física o lógica).
- Lógica de backend que analiza si el concepto tiene historial en otros periodos para decidir si se borra el registro o si solo se desactiva la plantilla de recurrencia.

## Capabilities

### New Capabilities
Ninguna.

### Modified Capabilities
- `gestion-conceptos`: Se añaden requisitos para la eliminación inteligente, definiendo los criterios de eliminación física vs. desactivación lógica de recurrencia.

## Impact

- `ConceptoRepository`: Requiere métodos para verificar la existencia de historial (`count_by_nombre`) y para eliminar registros o desactivar plantillas.
- `ConceptoService`: Implementación de la lógica de decisión "Eliminación Inteligente".
- `ConceptListFrame`: Adición de un botón de eliminación "🗑️" en cada fila de la tabla.
