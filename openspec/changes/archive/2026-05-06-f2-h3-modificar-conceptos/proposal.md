## Why

Los usuarios necesitan tener flexibilidad sobre sus registros financieros. Pueden cometer errores al momento de registrar un concepto o la información puede haber cambiado. Permitir la edición es fundamental para mantener la exactitud del Dashboard y de las finanzas.

## What Changes

- Permitir la modificación de un concepto financiero registrado previamente.
- Validación de los nuevos datos ingresados (valores positivos, nombre alfabético).
- Si el concepto es **recurrente**:
  - Modificar el **nombre** actualiza la plantilla recurrente que aplicará en periodos futuros (manteniendo intacto el histórico del periodo anterior).
  - Modificar el **valor** o el **tipo** afecta **únicamente** al registro en el periodo activo.

## Capabilities

### New Capabilities
Ninguna.

### Modified Capabilities
- `gestion-conceptos`: Se extienden los requisitos para incorporar escenarios de modificación en los conceptos existentes, diferenciando entre atributos regulares y actualizaciones de plantillas recurrentes.

## Impact

- `ConceptoService`: Requiere un nuevo método `modificar_concepto(id, nombre, valor, tipo)` y validaciones que contemplen el impacto en `plantillas_recurrentes`.
- `ConceptoRepository`: Requiere un método `update` en la base de datos.
- Interfaz de Usuario: La tabla `ConceptListFrame` o un nuevo componente modal deberá soportar el llenado con datos existentes para la edición (reaprovechando potencialmente `ConceptoForm`).
