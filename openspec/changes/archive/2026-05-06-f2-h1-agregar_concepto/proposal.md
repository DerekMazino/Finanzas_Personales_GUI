# Proposición: f2-h1-agregar_concepto

## Goal
Permitir al usuario registrar ingresos y egresos vinculados a un periodo específico, asegurando la integridad de los datos y permitiendo la creación de plantillas para conceptos recurrentes.

## Context
Tras implementar la gestión de periodos (F1), el siguiente paso natural es permitir que el usuario llene esos periodos con datos financieros. Esta HU es el núcleo de la gestión de transacciones.

## Scope
- Formulario de creación de conceptos en la UI.
- Validaciones de negocio (nombre, valor, tipo).
- Lógica de integración con periodos (creación automática si no existe).
- Persistencia en la tabla `conceptos` y `plantillas_recurrentes`.
