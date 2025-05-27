from django.db import models
from finanzas.models import Student

class Notification(models.Model):
    TYPE_CHOICES = [
        ('cuota_impaga', 'Cuota impaga'),
        ('asistencia_falta', 'Asistencia sin confirmar'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.get_type_display()} - {self.created_at.strftime("%d/%m/%Y")}'
