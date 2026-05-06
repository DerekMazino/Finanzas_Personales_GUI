# Tutorial de Uso: Gestión de Periodos

Este documento explica cómo utilizar la funcionalidad de gestión de periodos en la aplicación de Finanzas Personales.

## Inicio de la Aplicación

Al abrir la aplicación por primera vez cada mes, verás un mensaje emergente:

1. **Detección**: El sistema detecta que el periodo actual (ej. Mayo 2026) no existe en la base de datos.
2. **Confirmación**: Se te preguntará: *"El periodo X/2026 no existe. ¿Desea crearlo ahora?"*.
3. **Copia de Recurrentes**: Si seleccionas **SÍ**, el sistema:
    - Creará el registro del mes.
    - Buscará en los meses anteriores aquellos gastos o ingresos marcados como **Recurrentes**.
    - Los insertará automáticamente en el nuevo mes para que no tengas que volver a escribirlos.

## Consideraciones

- Cada mes es único. No puedes crear dos veces el mismo mes.
- Si decides no crear el periodo al inicio, podrás hacerlo más tarde desde el Dashboard (funcionalidad en desarrollo).

---
[Volver al README](../README.md)
