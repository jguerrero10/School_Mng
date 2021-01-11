from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout 
from django.urls import reverse
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
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
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)        
        if form.is_valid():
            first_name = request.POST.get('nombre')
            last_name = request.POST.get('apellido')
            email = request.POST.get('email')
            username = request.POST.get('num_id')
            rol = request.POST.get('rol')
            grupo = Group.objects.get(id = rol)
            user = User.objects.create_user(username, email, username, first_name=first_name, last_name=last_name)
            user.save()
            usuario = form.save(commit=False)
            usuario.user = user
            usuario.save()
            user.groups.add(grupo)
            messages.success(request, 'Usuario Guardado correctamente')
            return HttpResponseRedirect(reverse('crear_usuario'))
        else:
            error = form.errors
            messages.error(request, error)
            return HttpResponseRedirect(reverse('crear_usuario'))
    else:
        form = UsuarioForm()
        context = {'form': form}
        return render(request, 'director/crear_usuario.html', context)

@permission_required('school.is_director', login_url='/login/')
def leer_estudiantes(request):
    grupo = Group.objects.get(id=1)
    estudiantes = grupo.user_set.all()    
    context = {'estudiantes': estudiantes}
    return render(request, 'director/list_estudiantes.html', context)
