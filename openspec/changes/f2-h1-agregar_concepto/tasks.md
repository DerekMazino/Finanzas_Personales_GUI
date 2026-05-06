## 1. Setup y GitFlow

- [x] 1.1 **RULE-03**: Crear rama `feature/gestion-conceptos` desde `develop`.
- [x] 1.2 **RULE-03**: Crear rama `task/gestion-conceptos/HU-1` desde la feature.

## 2. Backend (Servicios y Repositorios)

- [x] 2.1 Crear `ConceptoService` con validaciones de nombre (regex) y valor (>0).
- [x] 2.2 Implementar lógica de "Auto-crear periodo" si no existe.
- [x] 2.3 Implementar lógica de guardado en `plantillas_recurrentes` si `es_recurrente` es true.

## 3. Frontend (UI)

- [x] 3.1 Crear `ConceptoForm` con validaciones visuales.
- [x] 3.2 Añadir botón "Agregar Concepto" en el Dashboard principal.
- [x] 3.3 Conectar el formulario con `ConceptoService`.

## 4. Pruebas y Calidad

- [x] 4.1 Unit tests para `ConceptoService` (validaciones y recurrencia).
- [x] 4.2 Verificación visual de flujos de éxito y error.

## 5. Finalización

- [ ] 5.1 **RULE-08**: Integración y limpieza de ramas.
- [ ] 5.2 **RULE-01**: Sincronización de README y Tutorial.
