## ADDED Requirements

### Requirement: Registro de Transacciones
El sistema debe permitir registrar conceptos de ingreso o egreso.

#### Scenario: Registro exitoso
- **GIVEN** Un periodo existente.
- **WHEN** El usuario ingresa un nombre válido (empieza por letra), un valor positivo y selecciona el tipo.
- **THEN** El sistema guarda el concepto en la base de datos vinculado al periodo.

#### Scenario: Periodo inexistente
- **WHEN** El usuario intenta registrar un concepto en un mes/año que no existe.
- **THEN** El sistema ofrece crear el periodo automáticamente.

#### Scenario: Concepto Recurrente
- **WHEN** El usuario marca un concepto como recurrente.
- **THEN** Se crea un registro en `plantillas_recurrentes` además del registro en `conceptos` del periodo actual.
