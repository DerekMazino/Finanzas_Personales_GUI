## 1. Setup y GitFlow

- [x] 1.1 **RULE-03**: Crear rama `task/gestion-periodos/HU-2` desde `feature/gestion-periodos`.
- [x] 1.2 **RULE-06**: Pre-flight check de la rama.

## 2. Lógica de Negocio (Servicios)

- [x] 2.1 Implementar `PeriodoService.obtener_todos_formateados()`.
- [x] 2.2 Agregar mapeo de meses (1 -> "Enero", etc.) en el servicio.
- [x] 2.3 Asegurar ordenamiento descendente por año y mes.

## 3. Interfaz de Usuario (CustomTkinter)

- [x] 3.1 Crear componente `PeriodListFrame` (ScrollableFrame).
- [x] 3.2 Implementar lógica para mostrar "Sin periodos" si la lista está vacía.
- [x] 3.3 Integrar el componente en el sidebar o área principal de `app.py`.

## 4. Pruebas y Validación

- [x] 4.1 Crear unit tests para el formateo y ordenamiento de la lista.
- [x] 4.2 Verificación visual de la lista con datos de prueba.

## 5. Finalización

- [ ] 5.1 **RULE-03**: Commit, Push y Merge hacia la rama feature.
- [ ] 5.2 **RULE-01**: Actualizar documentación si es necesario (tutorial.md).
