## Context
Se requiere una forma de navegar por la historia financiera. Actualmente el sistema solo detecta el mes actual, pero no permite ver el historial.

## Decisions

- **Repositorio**: Utilizar el método `get_all()` existente en `PeriodoRepository`.
- **Servicio**: Añadir `PeriodoService.listar_periodos()` que ordene y devuelva objetos mapeados (id, mes_nombre, anio).
- **UI**: 
    - Implementar un `ScrollableFrame` en la parte lateral o principal para mostrar la lista.
    - Cada elemento de la lista será un botón o etiqueta con el nombre del mes.
    - Traducir el número de mes (1-12) a nombres en español (Enero, Febrero...).

## Architecture
- `src/services/periodo_service.py`: Añadir lógica de ordenamiento y traducción de nombres de mes.
- `src/ui/components/period_list.py`: [NUEVO] Componente reutilizable de CustomTkinter para listar periodos.
