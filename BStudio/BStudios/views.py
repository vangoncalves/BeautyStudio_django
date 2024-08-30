from django.shortcuts import render
from .models import *

def index(request):
    """Página principal do Beauty Studio"""
    return render(request, 'BStudios/index.html')

def cursos(request):
    """Mostra todos as categorias do curso"""
    cacursos = CaCursos.objects.order_by('nome')
    context = {'cacursos': cacursos}
    return render(request, 'BStudios/cursos.html', context)

def servicos(request):
    """Mostra todos as categorias de serviços"""
    caservicos = CaServicos.objects.order_by('nome')
    context = {'caservicos': caservicos}
    return render(request, 'BStudios/servicos.html', context)