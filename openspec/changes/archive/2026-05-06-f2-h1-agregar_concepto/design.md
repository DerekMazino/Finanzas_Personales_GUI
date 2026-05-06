## Context
Se requiere una interfaz y lógica de servicio para manejar conceptos.

## Decisions

- **Servicio**: Crear `ConceptoService` para manejar la lógica de negocio (validaciones, creación de periodos on-the-fly, gestión de recurrentes).
- **Repositorio**: Utilizar `ConceptoRepository` para persistencia.
- **UI**: 
    - Crear `ConceptoForm` (un CTkFrame o CTkToplevel) para la entrada de datos.
    - Campos: Nombre (Entry), Valor (Entry), Tipo (SegmentedButton), Recurrente (Switch).
    - El periodo se seleccionará por defecto del Dashboard activo o se pedirá confirmación.

## Architecture
- `src/services/concepto_service.py`: [NUEVO] Lógica de validación y recurrencia.
- `src/ui/components/concepto_form.py`: [NUEVO] Formulario modal para agregar conceptos.
