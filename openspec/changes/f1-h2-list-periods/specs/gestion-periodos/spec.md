## ADDED Requirements

### Requirement: Visualización de Historial de Periodos
El sistema debe permitir al usuario ver un listado de todos los meses/años que han sido creados en el sistema.

#### Scenario: Existen periodos registrados
- **WHEN** El usuario accede a la sección de "Periodos".
- **THEN** El sistema muestra una lista con el Mes y Año de cada registro.
- **AND** El orden debe ser descendente (cronología inversa).

#### Scenario: No existen periodos
- **WHEN** La base de datos de periodos está vacía.
- **THEN** El sistema muestra un componente visual indicando la ausencia de datos y un botón de acción para crear el periodo actual.
