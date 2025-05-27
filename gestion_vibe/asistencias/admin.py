from django.contrib import admin
from .models import Asistencia

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('profesor', 'cpi', 'fecha', 'turno', 'estado', 'confirmado_por')
    list_filter = ('estado', 'turno', 'cpi', 'profesor')
    search_fields = ('profesor__username', 'cpi__nombre')
    date_hierarchy = 'fecha'
    ordering = ('-fecha', 'turno')

admin.site.register(Asistencia, AsistenciaAdmin)