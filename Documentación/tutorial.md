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

### Visualización en el Dashboard
El Dashboard está estructurado para mostrarte la información consolidada:
- **Resumen del Mes**: Verás los ingresos y gastos correspondientes al periodo que tienes seleccionado.
- **Lista de Conceptos**: Una tabla debajo mostrará todos los movimientos registrados para ese mes, incluyendo su valor, si son ingresos o egresos, y si son recurrentes.
- **Edición de Conceptos**: Al final de cada fila, encontrarás un botón "✏️". Si te equivocaste al registrar un concepto, puedes presionarlo para modificar sus datos. *Nota: Si cambias el nombre de un concepto recurrente, este cambio se aplicará a todos los meses futuros.*

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

## Visualización de Conceptos (Tabla del Dashboard)

Una vez que hayas agregado conceptos, la pantalla principal (Dashboard) mostrará una tabla con el detalle de las finanzas del mes actual:

- **Nombre:** La descripción del concepto.
- **Valor:** El monto en verde para ingresos y en rojo para egresos.
- **Tipo:** Identificación clara de Ingreso o Egreso.
- **Recurrente:** Indicador de si el concepto se clonará automáticamente en meses futuros.
- **Acción:** Botones para Editar (✏️) o Eliminar (🗑️).

Si el periodo no tiene conceptos, verás un mensaje invitándote a empezar a registrar tus movimientos.

## Eliminación de Conceptos (Eliminación Inteligente)

Para eliminar un concepto, presiona el botón "🗑️" al final de la fila. El sistema realizará una **Eliminación Inteligente** basándose en la historia del registro:

1.  **Eliminación Definitiva**: Si el concepto solo existe en el mes actual (fue un error puntual), se borrará completamente de la base de datos.
2.  **Desactivación de Recurrencia**: Si el concepto es recurrente y tiene historial en meses pasados, el sistema:
    - Borrará el registro del **mes actual**.
    - Eliminará la **plantilla de recurrencia** para que no aparezca en meses futuros.
    - **Conservará los registros pasados** intactos para no alterar tu historial histórico.

*Siempre se te pedirá confirmación antes de proceder, informándote de cuál de los dos casos se aplicará.*

---
[Volver al README](../README.md)
