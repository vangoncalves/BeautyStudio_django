from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos', views.cursos, name='cursos'),
    path('servicos', views.servicos, name='servicos'),
    path('cursos/<idCaCursos>/', views.curso, name='curso'),
    path('curso/<idCurso>/', views.detalhes, name='detalhes'),
    path('servicos/<idCaServicos>/', views.servico, name='servico'),
    path('agendamentos', views.agendamentos, name='agendamentos'),
]
