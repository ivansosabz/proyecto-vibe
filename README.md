# Vibe Cursillo - Sistema de Gestión

Este sistema está diseñado para gestionar la asistencia de profesores y el control de cuotas de los alumnos del cursillo Vibe. Está desarrollado con Django, y busca optimizar la administración de actividades y pagos en el entorno académico del cursillo.

## 👥 Tipos de usuarios

- **Profesor**: Puede registrar su asistencia indicando el CPI, turno, fecha, hora de inicio y fin.
- **Secretario**: Confirma la asistencia de los profesores.
- **Guido (Jefe)**: Tiene acceso total al sistema y puede supervisar todas las operaciones.

## 🕒 Registro de Asistencias

Cada vez que un profesor asiste a una clase, debe registrar su asistencia indicando:
- Curso preparatorio intensivo (CPI)
- Turno (mañana, tarde o noche)
- Fecha
- Hora de inicio
- Hora de fin

El secretario debe confirmar posteriormente esta asistencia.

## 💸 Registro de Cuotas

- Cada alumno pertenece a un **CPI** que define:
  - Nombre del curso (ej. CPI-2 Febrero)
  - Monto mensual
  - Período activo (ej. abril a febrero)

- El sistema registra el pago mensual de cada alumno.
- Si un alumno no ha pagado la cuota correspondiente a un mes, se genera una **notificación por falta de pago**.

## 🔧 Tecnologías utilizadas

- Backend: Django
- Base de datos: PostgreSQL
- Panel de administración: Django Admin
- Frontend: HTML + CSS + Bootstrap + JS simples

## 🚀 Objetivos

- Automatizar el control de asistencia y confirmación por parte del secretario.
- Generar alertas ante cuotas impagas.
- Facilitar el control administrativo del cursillo por parte de Guido.

## 📂 Estructura básica (propuesta)

