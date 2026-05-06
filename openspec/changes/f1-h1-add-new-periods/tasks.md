## 1. Setup y Control de Versiones

- [x] 1.1 **RULE-03**: Crear rama `feature/gestion-periodos` desde `develop`.
- [x] 1.2 **RULE-03**: Crear rama `task/gestion-periodos/HU-1` desde la rama feature.
- [x] 1.3 **RULE-06**: Realizar pre-flight check de la rama actual.

## 2. Capa de Datos (SQLite)

- [x] 2.1 Crear script de migración para la tabla `periodos` (id, mes, año).
- [x] 2.2 Actualizar el repositorio de conceptos para incluir la relación con el ID de periodo.
- [x] 2.3 Implementar el repositorio de `Periodos` usando el Query Builder liviano.

## 3. Lógica de Negocio (Servicios)

- [x] 3.1 Implementar `PeriodoService.verificar_existencia(mes, año)`.
- [x] 3.2 Implementar `PeriodoService.crear_periodo(mes, año)` con validación de unicidad.
- [x] 3.3 Implementar lógica de copia de conceptos recurrentes desde el último periodo.

## 4. Interfaz de Usuario (CustomTkinter)

- [x] 4.1 Crear el diálogo modal de confirmación: "¿Desea crear el periodo [Mes/Año]?".
- [x] 4.2 Conectar el flujo de inicio de la aplicación con la verificación del periodo actual.

## 5. Pruebas y Calidad

- [x] 5.1 Crear unit tests con `pytest` para la creación de periodos (incluyendo casos de duplicidad).
- [x] 5.2 Verificar que el formato de commit sea `feat(HU-1): {descripcion}`.

## 6. Finalización y Sincronización

- [ ] 6.1 **RULE-03**: Realizar commit, push y merge hacia `feature/gestion-periodos`.
- [ ] 6.2 **RULE-01**: Actualizar `README.md` y `Documentación/tutorial.md` con la nueva funcionalidad de periodos.
