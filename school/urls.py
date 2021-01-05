from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('matricula/', views.matricula_index, name='matricula'),
    path('matricula/crear', views.crear_matricula, name='crear_matricula'),
    path('estudiante/crear', views.crear_estudiante, name='crear_estudiante'),
    path('grupo/crear', views.crear_grupo, name='crear_grupo'),
    path('grupo/crear/curso', views.crear_curso, name='crear_curso')
]
