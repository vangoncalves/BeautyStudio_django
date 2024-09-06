#from django.shortcuts import render
#from django.http import HttpResponseRedirect
#from django.urls import reverse

# Create your views here.
#def arealogin(request):
#    """area login"""
#    if request.method != 'POST':
#        form = arealogin()
#    else:
#        form = arealogin(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('arealogin'))
#        
#    context = {'forms':form}
#    return render(request, 'BStudio/users/template/arealogin.html', context)
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def arealogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('arealogin.html')  # ou outra página após login
        else:
            return render(request, 'arealogin.html', {'error': 'Credenciais inválidas'})
    return render(request, 'arealogin.html')
