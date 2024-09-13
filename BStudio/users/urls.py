from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('arealogin/', views.arealogin, name='arealogin'),
    path('areacadastro/', views.areacadastro, name='areacadastro'),
    path('logout/', views.logout_view, name='logout'),
    
]

