## ADDED Requirements

### Requirement: Eliminación Inteligente de Conceptos
El sistema debe permitir eliminar un concepto del periodo actual, determinando automáticamente si se debe realizar una eliminación física completa o una desactivación lógica de la recurrencia para proteger el historial financiero.

#### Scenario: Eliminación física de concepto sin historial
- **GIVEN** Un concepto financiero que solo posee un registro en el periodo actual (sin historial en otros meses).
- **WHEN** El usuario confirma la eliminación.
- **THEN** El registro se elimina permanentemente de la base de datos y de la tabla de plantillas recurrentes (si aplicaba).

#### Scenario: Desactivación de recurrencia por historial (Eliminación lógica)
- **GIVEN** Un concepto marcado como recurrente que tiene registros asociados en meses previos.
- **WHEN** El usuario confirma la eliminación en el periodo actual.
- **THEN** El sistema elimina el registro únicamente del periodo activo Y marca la plantilla de recurrencia como "Inactiva" (o la elimina de la tabla de plantillas) para evitar su aparición en futuros periodos, preservando los registros históricos pasados.

#### Scenario: Confirmación obligatoria antes de eliminar
- **GIVEN** El usuario pulsa el botón de eliminación de un concepto.
- **WHEN** El sistema detecta la intención de borrado.
- **THEN** Se debe mostrar un mensaje de confirmación (pop-up) que informe al usuario si la acción será definitiva o si solo afectará a la recurrencia futura, antes de ejecutar cualquier cambio.
