from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('arealogin', auth_views.LoginView.as_view (template_name='users/arealogin.html'), name='arealogin'),
]

#removi um path
#removi uma importação