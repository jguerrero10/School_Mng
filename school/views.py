from django.shortcuts import render
from .forms import *

def home(request):
    return render(request, 'home.html')

def matricula_index(request):
    matriculas = Matricula.objects.all()
    context = {'matriculas': matriculas}
    return render(request, 'matricula/index.html', context)

def crear_matricula(request):
    form = MatriculaForm()
    context = {'form': form}
    return render(request, 'matricula/crear.html', context)
