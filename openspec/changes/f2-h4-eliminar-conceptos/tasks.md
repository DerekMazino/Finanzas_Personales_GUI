## 1. Setup y GitFlow

- [x] 1.1 **RULE-03**: Crear la rama `task/gestion-conceptos/HU-4` partiendo de la rama de feature activa.

## 2. Infraestructura y Repositorios

- [x] 2.1 En `QueryBuilder`, implementar el método `delete()` para generar sentencias SQL de borrado.
- [x] 2.2 En `ConceptoRepository`, añadir el método `delete_concepto(id)`.
- [x] 2.3 En `ConceptoRepository`, añadir el método `delete_plantilla_recurrente(nombre)`.
- [x] 2.4 En `ConceptoRepository`, añadir el método `count_history(nombre)` que retorne el conteo total de registros con ese nombre en la tabla `conceptos`.

## 3. Lógica de Negocio (Servicios)

- [x] 3.1 En `ConceptoService`, implementar `obtener_info_eliminacion(nombre)` que determine si la eliminación es física (conteo == 1) o lógica/recurrente (conteo > 1).
- [x] 3.2 En `ConceptoService`, implementar `eliminar_concepto(id, nombre, es_recurrente)` que ejecute el borrado del registro y de la plantilla si aplica.

## 4. Interfaz de Usuario (UI)

- [x] 4.1 En `ConceptListFrame`, añadir un botón "🗑️" (Eliminar) en la columna de Acciones.
- [x] 4.2 Implementar el método `confirmar_eliminacion(concepto)` en `ConceptListFrame` que use `messagebox.askyesno` con el mensaje dinámico del servicio.

## 5. Pruebas y Calidad

- [x] 5.1 En `test_concepto_service.py`, añadir tests para validar que la eliminación de un concepto recurrente con historial NO borra registros pasados.
- [x] 5.2 Validar que el conteo de historial funciona correctamente para decidir el tipo de mensaje al usuario.

## 6. Finalización

- [ ] 6.1 Realizar la integración de ramas según el protocolo.
- [ ] 6.2 Actualizar el archivo `tutorial.md` con la explicación sobre la eliminación inteligente de conceptos.
