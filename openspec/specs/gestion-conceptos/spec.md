# Gestión de Conceptos

## Purpose
<!-- TBD: Definir propósito completo de la gestión de conceptos -->
Gestionar la creación, modificación, y manipulación de conceptos (ingresos/egresos) financieros.

## Requirements

### Requirement: Modificar Concepto
El sistema debe permitir modificar los datos (nombre, valor, tipo) de un concepto existente en el periodo actual, respetando las validaciones correspondientes y propagando adecuadamente los cambios en caso de plantillas recurrentes.

#### Scenario: Modificación exitosa de atributos básicos
- **GIVEN** Un concepto financiero existente en el periodo actual.
- **WHEN** El usuario selecciona modificarlo y cambia su valor (a un número positivo) o su tipo.
- **THEN** El sistema guarda los cambios aplicándolos únicamente al registro de este periodo.

#### Scenario: Modificación de nombre en concepto recurrente
- **GIVEN** Un concepto etiquetado como "recurrente" en el periodo actual.
- **WHEN** El usuario modifica su nombre (comenzando por una letra del alfabeto).
- **THEN** El sistema actualiza el registro en el periodo activo Y actualiza la plantilla recurrente asociada, de modo que los futuros periodos tomen el nuevo nombre, sin afectar el nombre en periodos anteriores.

#### Scenario: Validación de datos fallida al modificar
- **GIVEN** El usuario se encuentra en el formulario de modificación de concepto.
- **WHEN** Ingresa un valor no numérico, un número negativo/cero, o un nombre inválido.
- **THEN** El sistema rechaza el cambio y emite un mensaje de error informativo al usuario sin guardar cambios en la base de datos.
