from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import *

class EstudianteForm(ModelForm):
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    num_id = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fec_nac = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))
    
    class Meta:
        model = Estudiante
        fields = '__all__'

class MatriculaForm(ModelForm):
    estudiante = forms.ModelChoiceField(queryset=Estudiante.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    curso = forms.ModelChoiceField(queryset=Grupo.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    estado = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))    
    class Meta:
        model = Matricula
        fields = '__all__'