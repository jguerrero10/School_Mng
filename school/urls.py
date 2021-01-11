from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('director/', views.index_director, name='home_director'),
    path('director/estudiantes/', views.leer_estudiantes, name='list_estudiantes'),   
    path('estudiante/', views.index_estudiante, name='home_estudiante'),
    path('profesor/', views.index_profesor, name='home_profesor'),
    path('director/usuario/crear', views.crear_usuario, name='crear_usuario')
    
]
