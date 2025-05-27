from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    ROLES = (
        ('PROF', 'Profesor'),
        ('SEC', 'Secretario'),
        ('ADMIN', 'Administrador'),
    )

    rol = models.CharField(max_length=5, choices=ROLES, default='PROF')
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_rol_display()})"

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'