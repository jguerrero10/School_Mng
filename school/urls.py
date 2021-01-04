from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('matricula/', views.matricula_index, name='matricula'),
    path('matricula/crear', views.crear_matricula, name='crear_matricula'),
    path('estudiante/crear', views.crear_estudiante, name='crear_estudiante')
]
