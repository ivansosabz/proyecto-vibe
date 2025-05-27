from django.contrib import admin
from .models import Pago

class PagoAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'cpi', 'mes', 'monto', 'metodo_pago', 'fecha_pago')
    list_filter = ('metodo_pago', 'cpi')
    search_fields = ('alumno__apellido', 'alumno__nombre')
    date_hierarchy = 'mes'
    ordering = ('-mes', 'alumno')

admin.site.register(Pago, PagoAdmin)