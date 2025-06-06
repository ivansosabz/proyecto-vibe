"""
URL configuration for gestion_vibe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gestion_vibe import views

admin.site.site_header = "Administración de Vibe"
admin.site.site_title = "Sistema Vibe"
admin.site.index_title = "Bienvenido al panel de administración"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('usuarios', include('usuarios.urls')),
    # path('notificaciones', include('notificaciones.urls')),
    # path('cursos', include('cursos.urls')),
    # path('finanzas', include('finanzas.urls')),
    # path('asistencias', include('asistencias.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
