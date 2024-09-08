from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('arealogin/', auth_views.LoginView.as_view (template_name='users/arealogin.html'), name='arealogin'),
    path('areacadastro/', views.areacadastro, name='areacadastro'),
    path('logout/', auth_views.LogoutView.as_view(next_page='arealogin'), name='logout'),
]

