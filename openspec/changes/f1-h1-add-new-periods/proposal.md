## Why

Implementar la capacidad de gestionar periodos mensuales para permitir una organización estructurada de las finanzas. Esto es fundamental para habilitar la recurrencia automática de conceptos y el cálculo de ahorros mensuales y acumulados, permitiendo al usuario tener claridad sobre su flujo de caja en el tiempo.

## What Changes

- Implementación de la lógica para detectar el periodo del mes actual al iniciar la aplicación.
- Creación de la funcionalidad para agregar nuevos periodos (Mes/Año).
- Lógica de copia automática de conceptos marcados como "Recurrentes" de periodos anteriores al nuevo periodo creado.
- Validación para evitar la creación de periodos duplicados.

## Capabilities

### New Capabilities
- `gestion-periodos`: Cubre la creación, validación y listado de periodos mensuales, incluyendo la transferencia de conceptos recurrentes.

### Modified Capabilities
- Ninguna.

## Impact

- Base de Datos: Se verá afectada la tabla de periodos y la lógica de inserción de conceptos.
- UI: Se requiere una vista o modal para la creación de periodos y un selector de periodos en el Dashboard.
- Lógica de Negocio: Nueva capa de servicios para la gestión de periodos y recurrencia.
