## 1. Setup y GitFlow

- [x] 1.1 **RULE-03**: Crear rama `feature/listar-conceptos` desde `develop`.
- [x] 1.2 **RULE-03**: Crear rama `task/listar-conceptos/HU-2` desde la feature.

## 2. Backend (Servicios y Repositorios)

- [x] 2.1 En `ConceptoRepository`, agregar `get_by_periodo_id(periodo_id)`.
- [x] 2.2 En `ConceptoService`, agregar `obtener_conceptos_por_periodo(mes, anio)`.

## 3. Frontend (UI)

- [x] 3.1 Crear el componente `ConceptListFrame` con el estado vacío manejado.
- [x] 3.2 Integrar `ConceptListFrame` en `App` para que se muestre en el área principal.
- [x] 3.3 Conectar la creación exitosa de concepto (en `ConceptoForm`) para que la lista se actualice en tiempo real.

## 4. Pruebas y Calidad

- [x] 4.1 Escribir test en `test_concepto_service.py` para asegurar que `obtener_conceptos_por_periodo` devuelve la lista correcta.
- [x] 4.2 Verificación visual (estado vacío vs lista poblada).

## 5. Finalización

- [x] 5.1 **RULE-08**: Integración y limpieza de ramas.
- [x] 5.2 **RULE-01**: Sincronización de README y Tutorial.
