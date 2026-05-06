# Propuesta: HU2 - Listar Periodos Registrados

## Descripción
Este incremento implementa la funcionalidad necesaria para que el usuario pueda visualizar una lista de todos los periodos (Mes/Año) almacenados en la base de datos. Es un paso crítico para permitir la navegación futura entre diferentes meses de gestión financiera.

## Objetivos
- Proveer una vista en la interfaz que liste de forma ordenada los periodos.
- Manejar el estado de "sin periodos" con un mensaje informativo y sugerencia de creación.
- Mantener la arquitectura modular (Repo -> Servicio -> UI).

## Criterios de Aceptación
- **CA1**: El sistema debe recuperar todos los periodos de la base de datos ordenados cronológicamente (más recientes primero).
- **CA2**: Si no existen periodos, la interfaz debe mostrar un mensaje: "No hay periodos registrados. ¡Crea el primero!".
- **CA3**: Los periodos deben mostrarse en un formato amigable (ej: "Mayo 2026").
