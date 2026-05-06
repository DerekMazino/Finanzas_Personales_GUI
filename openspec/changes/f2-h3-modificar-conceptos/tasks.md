## 1. Setup y GitFlow

- [x] 1.1 **RULE-03**: Asegurar que existe la rama de la feature correspondiente y crear la rama `task/gestion-conceptos/HU-3` a partir de ella.

## 2. Base de Datos y Repositorios

- [x] 2.1 En `ConceptoRepository`, añadir el método `update_concepto(id, nombre, valor, tipo, es_recurrente)`.
- [x] 2.2 En `ConceptoRepository`, añadir el método `update_plantilla_name(old_nombre, new_nombre)` para propagar los cambios en plantillas recurrentes.

## 3. Lógica de Negocio (Servicios)

- [x] 3.1 En `ConceptoService`, añadir el método `modificar_concepto(id, old_nombre, new_nombre, valor, tipo, es_recurrente)`.
- [x] 3.2 Implementar la lógica en `modificar_concepto` que evalúa si debe invocar a `update_plantilla_name` o simplemente a `update_concepto`.

## 4. Interfaz de Usuario (UI)

- [x] 4.1 En `ConceptListFrame`, añadir un botón "✏️" (Editar) al final de cada fila de concepto en la tabla.
- [x] 4.2 En `ConceptoForm`, agregar soporte en el constructor para recibir un `concepto_existente` (diccionario o tupla) y pre-llenar las entradas del formulario.
- [x] 4.3 Modificar el método `save()` de `ConceptoForm` para que llame a `modificar_concepto` si está en modo de edición.

## 5. Pruebas y Calidad

- [x] 5.1 En `test_concepto_service.py`, escribir tests que validen el cambio de un concepto regular.
- [x] 5.2 En `test_concepto_service.py`, escribir tests que validen que al cambiar el nombre de un concepto recurrente se invoca a la actualización de plantillas, pero si solo se cambia el valor no se invoca.

## 6. Finalización

- [ ] 6.1 Realizar la integración de ramas según GitFlow.
- [ ] 6.2 Actualizar el archivo `tutorial.md` con instrucciones sobre cómo editar conceptos.
