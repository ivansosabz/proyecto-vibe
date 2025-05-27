# gestion_vibe/views.py (o core/views.py si creaste una app)
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')