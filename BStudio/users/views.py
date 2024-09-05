from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def arealogin(request):
    """area login"""
    if request.method != 'POST':
        form = arealogin()
    else:
        form = arealogin(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('arealogin'))
        
    context = {'forms':form}
    return render(request, 'BStudio/users/template/arealogin.html', context)