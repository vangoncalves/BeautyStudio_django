from django.urls import path, include
from . import views


urlpatterns = [
    #Pagina inicial
    path('', views.index, name='index'),

    #Categoria de Cursos, adicionar, editar e excluir
    path('cursos', views.cursos, name='cursos'),
    path('cursosadd', views.cursosadd, name='cursosadd'),
    path('edit_cursos/<edit_idCaCursos>', views.edit_cursos, name='edit_cursos'),
    
    path('funcionarios', views.funcionarios, name='funcionarios'),
    path('funcionariosadd', views.funcionariosadd, name='funcionariosadd'),

    path('agendamentos', views.agendamentos, name='agendamentos'),

    #Cursos, adicionar, editar e excluir
    path('cursos/<idCaCursos>/', views.curso, name='curso'),
    path('curso/<idCurso>/', views.detalhes, name='detalhes'),
    path('cursoadd/<idCaCursos>', views.cursoadd, name='cursoadd'),
    path('edit_curso/<edit_idCurso>', views.edit_curso, name='edit_curso'),
    path('delete_curso/<excluir_curso>', views.excluir_curso, name='excluir_curso'),


    # Incluir as URLs do app 'users'
    path('users/', include('users.urls')),
    path('login/', include('django.contrib.auth.urls')), 

]
