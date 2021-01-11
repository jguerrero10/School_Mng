from django import forms
from django.db.models.base import Model
from django.forms import fields
from django.forms.models import ModelForm
from django.contrib.auth.models import Group
from .models import *

class UsuarioForm(ModelForm):
    nombre = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Nombre Completo'
    }))
    apellido = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Apellidos'
    }))
    email = forms.EmailField(max_length=80, required=False, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo Electrónico'
    }))
    rol = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select(attrs={
        'class': 'form-select',
    }))
    num_id = forms.CharField(max_length=11, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Documento de Identidad',
        'min': '10000000',
        'max': '99999999999'
    }))
    fec_nac = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control'
    }))

    class Meta:
        model = Usuario
        fields = ['rol', 'num_id', 'fec_nac'] 


