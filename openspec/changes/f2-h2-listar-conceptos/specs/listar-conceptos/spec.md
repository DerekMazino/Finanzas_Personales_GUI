## ADDED Requirements

### Requirement: Listado de Conceptos
El sistema debe mostrar los conceptos financieros de un periodo seleccionado.

#### Scenario: Visualización con datos
- **GIVEN** Un periodo seleccionado que contiene conceptos guardados.
- **WHEN** El usuario visualiza el Dashboard central.
- **THEN** Se muestra una tabla con las columnas: Nombre, Valor, Tipo y si es Recurrente.

#### Scenario: Visualización vacía
- **GIVEN** Un periodo que no tiene conceptos (recién creado).
- **WHEN** El usuario visualiza el Dashboard.
- **THEN** Se muestra el mensaje: "No hay conceptos registrados para este periodo. ¡Comienza agregando uno!".
