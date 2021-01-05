from django.shortcuts import render
from django.http import JsonResponse
from .forms import *

def home(request):
    return render(request, 'home.html')

def matricula_index(request):
    matriculas = Matricula.objects.all()
    context = {'matriculas': matriculas}
    return render(request, 'matricula/index.html', context)

def crear_matricula(request):
    formMatricula = MatriculaForm()    
    context = {'formMatricula': formMatricula}
    return render(request, 'matricula/crear.html', context)

def crear_estudiante(request):
    if request.method == 'POST': 
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'icon': 'success',
                        'title': 'Correcto!!!',
                        'text': 'Estudiante guardado correctamente.'}
            return JsonResponse(context)
        else:                  
            context = {'icon': 'error',
                        'title': 'Opps!!!',
                        'text': 'Problemas al guardar Estudiante, verifique los datos ingresados.'}
            return JsonResponse(context)    
    else:
        form = EstudianteForm()
        context = {'form': form}
        return render(request, 'estudiante/formEstudiante.html', context)

def crear_grupo(request):
    form = GrupoForm()
    context = {'formGrupo': form}
    return render(request, 'grupo/crear.html', context)

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'icon': 'success',
                        'title': 'Correcto!!!',
                        'text': 'Grado guardado correctamente.'}
            return JsonResponse(context)
        else:
            context = {'icon': 'error',
                        'title': 'Opps!!!',
                        'text': 'Problemas al guardar el Grado, Comuniquese con el admin.'}
            return JsonResponse(context)
    else:
        form = CursoForm()
        context = {'formCurso': form}
        return render(request, 'grupo/formCurso.html', context)
