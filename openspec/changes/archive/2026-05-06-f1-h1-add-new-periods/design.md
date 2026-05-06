## Context

El sistema actualmente carece de una gestión formal de periodos temporales, lo que dificulta la organización de transacciones por meses y la automatización de gastos fijos.

## Goals / Non-Goals

**Goals:**
- Proveer una base sólida para la persistencia de periodos en SQLite.
- Implementar la lógica de clonación de transacciones recurrentes.
- Garantizar que la interfaz de usuario sea intuitiva para la creación de periodos.

**Non-Goals:**
- Implementar edición de periodos ya creados (solo creación y eliminación lógica si fuera necesario).
- Gestión de metas de ahorro avanzadas (esto pertenece a otra feature).

## Decisions

- **Esquema de Base de Datos**: 
    - Tabla `periodos`: `id` (PK), `mes` (INT), `año` (INT).
    - Tabla `plantillas_recurrentes`: Para almacenar los conceptos que deben replicarse.
    - Tabla `conceptos`: Referencia a `periodos.id`.
- **Lógica de Negocio**: Al crear un periodo, se ejecutará un `INSERT INTO conceptos ... SELECT ... FROM plantillas_recurrentes`.
- **UI**: Uso de `CTkMessagebox` o un `CTkToplevel` personalizado para la sugerencia de creación de periodo.

## Risks / Trade-offs

- **Riesgo**: Duplicidad de conceptos si el proceso de creación falla a mitad.
- **Solución**: Usar transacciones SQL (BEGIN/COMMIT) para asegurar la integridad de la creación del periodo y sus conceptos asociados.
- **Trade-off**: Simplicidad sobre flexibilidad. Por ahora, los periodos son estrictamente mensuales.
