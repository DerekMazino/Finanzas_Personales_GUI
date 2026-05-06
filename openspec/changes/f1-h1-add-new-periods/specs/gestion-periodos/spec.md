## ADDED Requirements

### Requirement: Detección Automática de Periodo Actual
El sistema debe verificar automáticamente al inicio si el periodo correspondiente al mes y año actuales ya existe en la base de datos.

#### Scenario: Periodo actual no existe
- **WHEN** El usuario abre la aplicación y no hay un registro para el mes/año actual.
- **THEN** El sistema debe mostrar un mensaje sugiriendo la creación del nuevo periodo (S/N).

### Requirement: Creación de Nuevo Periodo con Recurrencia
Al crear un nuevo periodo, el sistema debe poblarlo automáticamente con los conceptos marcados como recurrentes de periodos previos.

#### Scenario: Usuario acepta crear periodo
- **WHEN** El usuario selecciona "Sí" para crear el periodo.
- **THEN** El sistema crea el registro del periodo y busca conceptos marcados como 'Recurrente' en el último periodo registrado para copiarlos al nuevo.

### Requirement: Validación de Unicidad de Periodos
Cada periodo definido por el par Mes/Año debe ser único en el sistema.

#### Scenario: Intento de duplicación
- **WHEN** Se intenta crear un periodo (ej. 05/2026) que ya existe en la base de datos.
- **THEN** El sistema debe impedir la creación e informar al usuario que el periodo ya está registrado.
