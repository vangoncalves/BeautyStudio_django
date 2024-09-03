from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos', views.cursos, name='cursos'),
    path('cursos/<idCaCursos>/', views.curso, name='curso'),
    path('curso/<idCurso>/', views.detalhes, name='detalhes'),
    path('agendamentos', views.agendamentos, name='agendamentos'),
]
