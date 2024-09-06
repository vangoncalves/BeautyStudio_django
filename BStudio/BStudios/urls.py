from django.urls import path, include
from . import views


urlpatterns = [
    #Pagina inicial
    path('', views.index, name='index'),


    path('cursos', views.cursos, name='cursos'),
    path('cursosadd', views.cursosadd, name='cursosadd'),
    path('edit_cursos/<edit_idCaCursos>', views.edit_cursos, name='edit_cursos'),
    


    path('agendamentos', views.agendamentos, name='agendamentos'),

    path('cursos/<idCaCursos>/', views.curso, name='curso'),
    path('curso/<idCurso>/', views.detalhes, name='detalhes'),
    path('cursoadd/<idCaCursos>', views.cursoadd, name='cursoadd'),
    path('edit_curso/<edit_idCurso>', views.edit_curso, name='edit_curso'),
      # Incluir as URLs do app 'users'
    path('users/', include('users.urls')),
    path('login/', include('django.contrib.auth.urls')), 

]
