from django.urls import path
from . import views

urlpatterns = [
    path('arealogin/', views.arealogin, name='arealogin'),
    path('areacadastro/', views.areacadastro, name='areacadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('areacadastroadmin/', views.areacadastroadmin, name='areacadastroadmin'),
    
]

