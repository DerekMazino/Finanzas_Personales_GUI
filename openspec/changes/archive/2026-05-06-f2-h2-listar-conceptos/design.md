## Context
Se requiere listar visualmente los conceptos en el Dashboard y recuperarlos desde la base de datos por periodo.

## Decisions
- **Repositorio**: Añadir método `get_by_periodo_id(periodo_id)` en `ConceptoRepository`.
- **Servicio**: Añadir método `obtener_conceptos_por_periodo(mes, anio)` en `ConceptoService`.
- **UI**: 
    - Crear `ConceptListFrame` (un `CTkScrollableFrame` que actuará como tabla).
    - Cada fila será un frame interno con etiquetas para: Nombre, Valor, Tipo y un indicador de Recurrencia.
    - El Dashboard principal (`App`) cargará los conceptos usando `ConceptoService` y los inyectará en `ConceptListFrame`.
    - Si la lista está vacía, se mostrará un `CTkLabel` con el texto de estado vacío.

## Architecture
- `src/ui/components/concept_list.py`: [NUEVO] Componente visual para la lista/tabla.
- `src/services/concepto_service.py`: [MODIFICAR] Añadir lógica de consulta.
- `src/database/concepto_repository.py`: [MODIFICAR] Añadir consulta SQL por `periodo_id`.
