from django import forms
from django.forms import fields
from .models import *

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellidos = forms.CharField(max_length=60)
    num_id = forms.CharField(max_length=11)
    fec_nac = forms.DateField()
    
    class Meta:
        model = Estudiante
        fields = '__all__'

class MatriculaForm(forms.Form):
    estudiante = forms.ModelChoiceField(queryset=Estudiante.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    curso = forms.ModelChoiceField(queryset=Grupo.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    estado = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))    
    class Meta:
        model = Matricula
        fields = '__all__'