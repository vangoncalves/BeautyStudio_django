from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def arealogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index.html')  #colocar a pagina que o user vai após login
        else:
            return render(request, 'arealogin.html', {'error': 'Credenciais inválidas'})
    return render(request, 'arealogin.html')

def areacadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  #Login automático após cadastro
            return redirect('index.html')  #Redireciona para a página inicial após login, pode ser mudado isso!!!
    else:
        form = UserCreationForm()
    return render(request, 'users/areacadastro.html', {'form': form})
