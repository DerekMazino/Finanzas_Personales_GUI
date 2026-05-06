# Proposición: f2-h2-listar-conceptos

## Goal
Permitir al usuario visualizar todos los conceptos (ingresos y egresos) registrados en un periodo específico a través de una tabla en el Dashboard.

## Context
Después de permitir la creación de conceptos (HU1), el usuario necesita ver reflejados estos datos en la interfaz principal. La lista de conceptos es esencial para entender el flujo de dinero en un mes determinado.

## Scope
- Creación de un componente UI tipo tabla (`ConceptListFrame`) en el Dashboard.
- Método en `ConceptoService` para recuperar conceptos por periodo.
- Estado vacío ("No hay conceptos registrados...").
- Columnas a mostrar: Nombre, Valor, Tipo, Recurrente (y fecha si está disponible).
