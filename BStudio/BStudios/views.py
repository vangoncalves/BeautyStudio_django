from django.shortcuts import render
from .models import *
from .forms import UsuarioForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    """Página principal do Beauty Studio"""
    return render(request, 'BStudios/index.html')



def cursos(request):
    """Mostra todos as categorias do curso"""
    cacursos = CaCursos.objects.order_by('nome')
    context = {'cacursos': cacursos}
    return render(request, 'BStudios/cursos.html', context)

def curso(request, idCaCursos):
    """Mostra um unico curso e todas as suas entradas"""
    curso = CaCursos.objects.get(idCaCursos = idCaCursos)
    cursos = curso.curso_set.order_by('-nome')
    context ={'curso': curso, 'cursos':cursos}
    return render(request, 'BStudios/curso.html', context)

def detalhes(request, idCurso):
    """Mostra um unico curso e todas as suas entradas"""
    detalhe = Curso.objects.get(idCurso = idCurso)
    context ={'detalhe':detalhe}
    return render(request, 'BStudios/curso_detalhes.html', context)



def servicos(request):
    """Mostra todos as categorias de serviços"""
    caservicos = CaServicos.objects.order_by('nome')
    context = {'caservicos': caservicos}
    return render(request, 'BStudios/servicos.html', context)

def servico(request, idCaServicos):
    """Mostra um unico servico e todas as suas entradas"""
    servico = CaServicos.objects.get(id = idCaServicos)
    servicos = servico.servico_set.order_by('-nome')
    context ={'servico': servico, 'servicos':servicos}
    return render(request, 'BStudios/servico.html', context)



def agendamentos(request):
    """Agenda um curso"""
    if request.method != 'POST':
        form = UsuarioForm()
    else:
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('agendamentos'))
        
    context = {'forms':form}
    return render(request, 'BStudios/agendamentos.html', context)
