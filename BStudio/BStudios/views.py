from django.shortcuts import render
from .models import *
from .forms import CursoForm, CaCursosForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    """Página principal do Beauty Studio"""
    return render(request, 'BStudios/index.html')



def cursos(request):
    """Mostra todas as categorias do curso"""
    cacursos = CaCursos.objects.order_by('nome')
    context = {'cacursos': cacursos}
    return render(request, 'BStudios/cursos.html', context)

def cursosadd(request):
    """Adiciona uma nova categoria de curso."""
    if request.method != 'POST':
        form = CaCursosForm()
    else:
        form = CaCursosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cursos'))
        
    context = {'form':form}
    return render(request, 'BStudios/cursos_add.html', context)

def edit_cursos(request, edit_idCaCursos):
    """Edita uma entrada existente"""
    edit = CaCursos.objects.get(idCaCursos=edit_idCaCursos)

    if request.method != 'POST':
        form = CaCursosForm(instance=edit)

    else:
        form = CaCursosForm(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cursos'))
    
    context ={'edit':edit, 'form':form}
    return render(request, 'BStudios/edit_cursos.html', context)



def curso(request, idCaCursos):
    """Mostra uma unica categoria e todos os seus cursos"""
    curso = CaCursos.objects.get(idCaCursos = idCaCursos)
    cursos = curso.curso_set.order_by('-nome')
    context ={'curso': curso, 'cursos':cursos}
    return render(request, 'BStudios/curso.html', context)

def cursoadd(request, idCaCursos):
    """Adiciona um novo curso."""
    cursos = CaCursos.objects.get(idCaCursos=idCaCursos)

    if request.method != 'POST':
        form = CursoForm()
    else:
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            cursoadd = form.save(commit=False)
            cursoadd.fk_idCaCursos = cursos
            cursoadd.save()
            return HttpResponseRedirect(reverse('curso', args=[idCaCursos]))
        
    context = {'cursos':cursos,'form':form}
    return render(request, 'BStudios/curso_add.html', context)

"""Nao ta pronto"""
def edit_curso(request, edit_idCurso):
    """Edita uma entrada existente"""
    edit = Curso.objects.get(idCurso=edit_idCurso)
    curso = Curso.fk_idCaCursos

    if request.method != 'POST':
        form = CursoForm(instance=edit)

    else:
        form = CursoForm(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detalhes', args=[edit.idCurso]))
    
    context = {'edit': edit, 'curso': curso, 'form': form}

    return render(request, 'BStudios/edit_curso.html', context)

def detalhes(request, idCurso):
    """Mostra um unico curso e todas as suas entradas"""
    detalhe = Curso.objects.get(idCurso = idCurso)
    context ={'detalhe':detalhe}
    return render(request, 'BStudios/curso_detalhes.html', context)


"""Não está pronto"""
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




