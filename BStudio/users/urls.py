from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('arealogin', auth_views.LoginView.as_view (template_name='BStudio/users/arealogin.html'), name='login'),
]