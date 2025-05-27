from django.db import models
from cursos.models import Alumno, CPI
from django.utils import timezone


class Pago(models.Model):
    METODOS = (
        ('EF', 'Efectivo'),
        ('TR', 'Transferencia'),
        ('TB', 'Tarjeta Bancaria'),
        ('OT', 'Otro'),
    )

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='pagos')
    cpi = models.ForeignKey(CPI, on_delete=models.CASCADE)
    mes = models.DateField()  # Usamos el primer día del mes para representar el mes completo
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=2, choices=METODOS)
    fecha_pago = models.DateField(default=timezone.now)
    comprobante = models.CharField(max_length=50, blank=True)
    registrado_por = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Pago de {self.alumno} - {self.mes.strftime('%B %Y')}"

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['-mes', 'alumno']
        unique_together = ['alumno', 'mes']