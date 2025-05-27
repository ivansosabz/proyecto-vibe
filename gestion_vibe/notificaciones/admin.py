from django.contrib import admin
from .models import Notificacion

class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'mensaje', 'leida', 'fecha_creacion')
    list_filter = ('tipo', 'leida', 'usuario')
    search_fields = ('mensaje', 'usuario__username')
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)

admin.site.register(Notificacion, NotificacionAdmin)