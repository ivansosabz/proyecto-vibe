from django.db import models
from usuarios.models import Usuario
from cursos.models import Alumno
from asistencias.models import Asistencia
from finanzas.models import Pago


class Notificacion(models.Model):
    TIPOS = (
        ('PAGO', 'Pago pendiente'),
        ('ASIST', 'Asistencia pendiente'),
        ('GEN', 'General'),
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificaciones')
    tipo = models.CharField(max_length=5, choices=TIPOS)
    mensaje = models.TextField()
    relacion_asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE, null=True, blank=True)
    relacion_pago = models.ForeignKey(Pago, on_delete=models.CASCADE, null=True, blank=True)
    relacion_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)
    fecha_leida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Notificación para {self.usuario} - {self.get_tipo_display()}"

    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        ordering = ['-fecha_creacion']