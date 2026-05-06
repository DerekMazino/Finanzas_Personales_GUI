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

## Visualización de Periodos

En la barra lateral izquierda de la aplicación, encontrarás la sección **PERIODOS**:

1. **Listado Cronológico**: Verás todos los meses registrados ordenados del más reciente al más antiguo.
2. **Estado Vacío**: Si aún no has creado ningún periodo, verás un mensaje invitándote a crear el primero.
3. **Navegación**: Puedes hacer clic en los botones de la lista para cambiar la vista del Dashboard al periodo seleccionado (funcionalidad de filtrado en desarrollo).

## Gestión de Conceptos

Para registrar un nuevo ingreso o gasto:

1. Ve al Dashboard principal.
2. Haz clic en el botón **➕ Agregar Concepto**.
3. Completa el formulario con:
   - **Nombre**: Debe empezar por una letra (ej. Sueldo, Alquiler).
   - **Valor**: Un número positivo.
   - **Tipo**: Ingreso o Egreso.
   - **Recurrente**: Si marcas esta opción, el concepto se guardará como plantilla y se aplicará automáticamente a todos los nuevos periodos que crees en el futuro.
4. Haz clic en **Guardar**.

---
[Volver al README](../README.md)
