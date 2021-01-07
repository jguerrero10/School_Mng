from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout 
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *

def login_(request):
    if request.method == 'POST':
        username = request.POST.get('inputUser')
        password = request.POST.get('inputPassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            return HttpResponse('Error en el usuario')

    else:
        return render(request, 'accounts/login.html')

@login_required(login_url='/login/')
def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required(login_url='/login/')
def home(request):
    user = request.user
    if user.has_perm('school.is_student'):
        return HttpResponseRedirect(reverse('home_estudiante'))
    elif user.has_perm('school.is_teacher'):
        return HttpResponseRedirect(reverse('home_profesor'))
    elif user.has_perm('school.is_director'):
        return HttpResponseRedirect(reverse('home_director'))
    else:
        return HttpResponse('No tiene acceso')

@permission_required('school.is_director')
def index_director(request):
    return render(request, 'director/index.html')

@permission_required('school.is_student')
def index_estudiante(request):
    return render(request, 'estudiante/index.html')

@permission_required('school.is_teacher')
def index_profesor(request):
    return render(request, 'profesor/index.html')

@permission_required('school.is_director', login_url='/login/')
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
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'icon': 'success',
                        'title': 'Correcto!!!',
                        'text': 'Grupo guardado correctamente.'}
            print(context)
            return JsonResponse(context)
        else:
            context = {'icon': 'error',
                        'title': 'Opps!!!',
                        'text': 'Problemas al guardar el Grupo, verifique los datos ingresados.'}
            return JsonResponse(context)
    else:
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

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'icon': 'success',
                        'title': 'Correcto!!!',
                        'text': 'Grado guardado correctamente.'}
            return JsonResponse(context)
        else:
            context = {'icon': 'error',
                        'title': 'Opps!!!',
                        'text': 'Problemas al guardar Profesor, verifique los datos ingresados.'}
            return JsonResponse(context)
            
    else:
        formProfesor = ProfesorForm()
        context = {'formProfesor': formProfesor}
        return render(request, 'profesor/formProfesor.html', context)
