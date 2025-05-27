from django.db import models
from django.utils import timezone


class CPI(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    monto_cuota = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    @property
    def duracion(self):
        return (self.fecha_fin - self.fecha_inicio).days

    class Meta:
        verbose_name = 'CPI'
        verbose_name_plural = 'CPIs'
        ordering = ['-fecha_inicio']


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cpi = models.ForeignKey(CPI, on_delete=models.SET_NULL, null=True, related_name='alumnos')
    fecha_inscripcion = models.DateField(default=timezone.now)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (CPI: {self.cpi})"

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        ordering = ['apellido', 'nombre']