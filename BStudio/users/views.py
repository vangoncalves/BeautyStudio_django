from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import UsuarioRegistrationForm, SuperUserCreationForm
from .models import Usuario
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def arealogin(request):
    if request.method == "POST":
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('master.html')  #colocar a pagina que o user vai após login
        else:
             context = {'error': 'Credenciais inválidas'}
             return render(request, 'users/arealogin.html', context)
    return render(request, 'users/arealogin.html')

def areacadastro(request):
    if request.method == 'POST':
        form = UsuarioRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save() 
            messages.success(request, f'Bem-vindo, {user.username}! Seu cadastro foi realizado com sucesso.')
            return redirect('arealogin')  # Redireciona para a página de login
    else:
        form = UsuarioRegistrationForm()
    return render(request, 'users/areacadastro.html', {'form': form})

def logout_view(request):
    """Faz logout do usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('index')) # Redireciona para a página index após o logout

@login_required
def areacadastroadmin(request):
    if request.method == 'POST':
        form = SuperUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_staff = True  # Marca como superusuário ou staff
            user.is_superuser = True
            user.save()
            return redirect('arealogin')  # Redireciona para a área de login ou qualquer outra página
    else:
        form = SuperUserCreationForm()
    
    return render(request, 'users/areacadastroadmin.html', {'form': form})
