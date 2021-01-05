from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import *

grado_CHOICES = [
        ('0', 'Transición'),
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'),
        ('6', 'Sexto'),
        ('7', 'Séptimo'),
        ('8', 'Octavo'),
        ('9', 'Noveno'),
        ('10', 'Décimo'),
        ('11', 'Undécimo')
    ]

class EstudianteForm(ModelForm):
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    num_id = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fec_nac = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    
    class Meta:
        model = Estudiante
        fields = '__all__'

class ProfesorForm(ModelForm):
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    num_id = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profesor
        fields = '__all__'

class CursoForm(ModelForm):    
    grado = forms.ChoiceField(choices=grado_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Curso
        fields = '__all__'

class GrupoForm(ModelForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    nombre = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dir_grupo = forms.ModelChoiceField(queryset=Profesor.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Grupo
        fields = '__all__'

class MatriculaForm(ModelForm):
    estudiante = forms.ModelChoiceField(queryset=Estudiante.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    curso = forms.ModelChoiceField(queryset=Grupo.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    estado = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'type': 'checkbox'}))    
    class Meta:
        model = Matricula
        fields = '__all__'