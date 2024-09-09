from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from .forms import UsuarioRegistrationForm
from .models import Usuario
from django.contrib.auth import logout


def arealogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  #colocar a pagina que o user vai após login
        else:
            return render(request, 'arealogin.html', {'error': 'Credenciais inválidas'})
    return render(request, 'arealogin.html')

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
    logout(request)
    return redirect('index.html')  # Redireciona para a página de login após o logout

