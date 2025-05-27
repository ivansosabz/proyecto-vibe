from django.db import models
from usuarios.models import Usuario
from cursos.models import CPI


class Asistencia(models.Model):
    TURNOS = (
        ('M', 'Mañana'),
        ('T', 'Tarde'),
        ('N', 'Noche'),
    )

    ESTADOS = (
        ('P', 'Pendiente'),
        ('C', 'Confirmada'),
        ('R', 'Rechazada'),
    )

    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'PROF'})
    cpi = models.ForeignKey(CPI, on_delete=models.CASCADE)
    fecha = models.DateField()
    turno = models.CharField(max_length=1, choices=TURNOS)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')
    confirmado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='asistencias_confirmadas', limit_choices_to={'rol': 'SEC'})
    fecha_confirmacion = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Asistencia {self.get_estado_display()} - {self.profesor} - {self.fecha}"

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        ordering = ['-fecha', 'turno']
        unique_together = ['profesor', 'fecha', 'turno']