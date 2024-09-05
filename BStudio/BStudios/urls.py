from django.urls import path
from . import views

urlpatterns = [
    #Pagina inicial
    path('', views.index, name='index'),


    path('cursos', views.cursos, name='cursos'),
    path('cursos/<idCaCursos>/', views.curso, name='curso'),
    path('cursosadd', views.cursosadd, name='cursosadd'),
    path('edit_cursos/<idCaCursos>', views.edit_cursos, name='edit_cursos'),
    


    path('agendamentos', views.agendamentos, name='agendamentos'),

    path('curso/<idCurso>/', views.detalhes, name='detalhes'),
    path('cursoadd/<idCaCursos>', views.cursoadd, name='cursoadd'),
    path('edit_curso/<edit_id>', views.edit_curso, name='edit_curso'),
    


    path('arealogin', views.arealogin, name='arealogin'), #adicionado  por david
]
