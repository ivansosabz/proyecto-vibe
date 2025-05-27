from django.contrib import admin
from .models import CPI, Alumno

class CPIAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'monto_cuota', 'fecha_inicio', 'fecha_fin', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre',)
    ordering = ('-fecha_inicio',)

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'cpi', 'activo')
    list_filter = ('cpi', 'activo')
    search_fields = ('apellido', 'nombre', 'dni')
    raw_id_fields = ('cpi',)
    ordering = ('apellido', 'nombre')

admin.site.register(CPI, CPIAdmin)
admin.site.register(Alumno, AlumnoAdmin)