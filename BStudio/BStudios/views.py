from django.shortcuts import render, redirect
from .models import *
from .forms import CursoForm, CaCursosForm, MetodoPagamentoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    """Página principal do Beauty Studio"""
    #Verifica se a mensagem deve ser exibida
    show_welcome = request.session.pop('show_welcome', False)
    username = request.session.get('username', 'Usuario')

    cursos = Curso.objects.all()

    context = {
        'show_welcome': show_welcome,
        'username': username,
        'cursos': cursos,
    }
    return render(request, 'BStudios/index.html', context)



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
        
    context = {'form':form }
    return render(request, 'BStudios/cursos_add.html', context)

def edit_cursos(request, edit_idCaCursos):
    """Edita categoria existente"""
    edit = CaCursos.objects.get(idCaCursos=edit_idCaCursos)

    if request.method != 'POST':
        form = CaCursosForm(instance=edit)

    else:
        form = CaCursosForm(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cursos'))
    
    context ={'edit':edit, 'form':form }
    return render(request, 'BStudios/edit_cursos.html', context)

def excluir_cursos(request, idCaCursos):
    """Exclui categoria de cursos"""
    cursos = CaCursos.objects.get(idCaCursos=idCaCursos)

    if request.method == 'POST':
        cursos.delete()
        messages.success(request, 'Categoria deletada com sucesso!')
        return HttpResponseRedirect(reverse('cursos'))
    context = {'cursos':cursos}
    return render(request, 'BStudios/delete_cursos.html', context)



def curso(request, idCaCursos):
    """Mostra uma unica categoria e todos os seus cursos"""
    curso = CaCursos.objects.get(idCaCursos = idCaCursos)
    cursos = curso.curso_set.order_by('-nome')
    context ={'curso': curso, 'cursos':cursos}
    return render(request, 'BStudios/curso.html', context)

def cursoadd(request, idCaCursos):
    """Adiciona um novo curso."""
    categorias = CaCursos.objects.all()
    funcionarios = Funcionario.objects.all()
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
        
    context = {'cursos':cursos,'form':form, 'categorias':categorias, 'funcionarios':funcionarios}
    return render(request, 'BStudios/curso_add.html', context)

def edit_curso(request, idCurso):
    """Edita um curso de uma determinada categoria existente"""
    categorias = CaCursos.objects.all()
    funcionarios = Funcionario.objects.all()
    edit = Curso.objects.get(idCurso=idCurso)
    curso = Curso.fk_idCaCursos

    if request.method != 'POST':
        form = CursoForm(instance=edit)

    else:
        form = CursoForm(request.POST, request.FILES, instance=edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detalhes', args=[edit.idCurso]))
    
    context = {'edit': edit, 'curso': curso, 'form': form, 'categorias':categorias, 'funcionarios':funcionarios}

    return render(request, 'BStudios/edit_curso.html', context)

def detalhes(request, idCurso):
    """Mostra detalhes de um unico curso de uma determinada categoria"""
    detalhe = Curso.objects.get(idCurso = idCurso)

    # Verifica se a chave 'historico_cursos' já existe na sessão
    if 'historico_cursos' not in request.session:
        request.session['historico_cursos'] = []

    # Obtém o histórico da sessão
    historico = request.session['historico_cursos']

    # Adiciona o curso ao histórico, se ele ainda não estiver lá
    if detalhe.idCurso not in historico:
        historico.append(detalhe.idCurso)

    # Limita o histórico a 10 cursos
    if len(historico) > 10:
        historico.pop(0)  # Remove o curso mais antigo

    # Atualiza o histórico na sessão
    request.session['historico_cursos'] = historico

    # Renderiza a página de detalhes do curso
    context ={'detalhe':detalhe}
    return render(request, 'BStudios/curso_detalhes.html', context)

def excluir_curso(request, idCurso):
    """Excluir um curso de uma determinada categoria"""
    curso = Curso.objects.get(idCurso=idCurso)
    idCaCursos = curso.fk_idCaCursos.idCaCursos

    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso deletado com sucesso!')
        return HttpResponseRedirect(reverse('curso', args=[idCaCursos]))
    context = {'cursos':curso}
    return render(request, 'BStudios/delete_curso.html', context)


@login_required # Para isso acontecer, o usuario deve estar logado
def perfil(request):
    """Perfil do usuario"""
    historico_ids = request.session.get('historico_cursos', [])

    # Busca os cursos correspondentes aos IDs armazenados no histórico
    cursos_historico = Curso.objects.filter(idCurso__in=historico_ids)
    
    user = request.user  # Obtém o usuário logado

    if  user.is_superuser:
        pedido = Pedido.objects.all()
    else:
        pedido = Pedido.objects.filter(fk_idUsuario=request.user)

    context={'pedido': pedido, 'cursos_historico':cursos_historico}
    return render(request, 'BStudios/perfil.html', context) 
       
@login_required
def comprar_pedido(request, idCurso):
    """Metodo para comprar cursos"""
    curso = Curso.objects.get(idCurso=idCurso)

    # Verifica se o usuário já comprou o curso
    if Pedido.objects.filter(fk_idUsuario=request.user, fk_idCurso=curso).exists():
        return render(request, 'BStudios/ja_comprou.html', {'curso': curso})

    if request.method == 'POST':
        form = MetodoPagamentoForm(request.POST)
        if form.is_valid():
            metodo_pagamento = form.cleaned_data['metodo_pagamento']
        
        compra = Pedido(
            fk_idCaCursos=curso.fk_idCaCursos,
            fk_idUsuario=request.user,
            fk_idCurso=curso,
            fk_idMetodoPagamento=metodo_pagamento 
        )
        compra.save()
        return redirect('perfil')

    form = MetodoPagamentoForm()
    context = {'curso':curso, 'form':form}
    return render(request, 'BStudios/confirmar_compra.html', context)


