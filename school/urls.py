from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('matricula/', views.matricula_index, name='matricula'),
    path('matricula/crear/', views.crear_matricula, name='crear_matricula'),
    path('estudiante/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('grupo/crear/', views.crear_grupo, name='crear_grupo'),
    path('grupo/crear/curso/', views.crear_curso, name='crear_curso'),
    path('profesor/crear/', views.crear_profesor, name='crear_profesor'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('estudiante/', views.index_estudiante, name='home_estudiante'),
    path('profesor/', views.index_profesor, name='home_profesor'),
    path('director/', views.index_director, name='home_director'),
]
