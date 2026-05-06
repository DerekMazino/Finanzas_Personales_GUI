# Proyecto: Finanzas Personales

## Overview
Este proyecto es un GUI de gestion de ingresos y gastos para finanzas personales. Permitira saber cuanto dinero se tiene y en que se gasta. Permitirá controlar un ahorro para un objetivo futuro. Este proyecto será la base para un proyecto mas grande que permita gestionar finanzas personales.

## Tech Stack
- Python

## Objetivos de diseño
- GUI limpio y moderno.
- Layout de dashboard.
- Componentes simples y legibles.

## Limitaciones de alcance
- No autenticación.

## Lógica de negocio
- **Periodos**: Los periodos son estrictamente mensuales (Mes/Año). El sistema debe permitir la creación de periodos basados en el calendario.
- **Ahorro Acumulado**: El sistema siempre debe calcular el ahorro del mes (Ingresos - Egresos) y el ahorro acumulado de todos los periodos. La Meta de Ahorro es opcional; si se define, se muestra el progreso hacia ella, de lo contrario, solo se muestran los totales ahorrados.
- **Recurrencia**: Los conceptos (Ingresos/Egresos) marcados como recurrentes deben ser creados automáticamente al generar un nuevo periodo, manteniendo su nombre y tipo, pero permitiendo que el valor sea ajustado individualmente en cada periodo.

## Objetivo de este proyecto
Este proyecto es para explorar como definir un sistema usando OpenSpec y generar un GUI usando IA.
