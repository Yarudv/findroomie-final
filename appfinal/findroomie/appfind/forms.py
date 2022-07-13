from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Publicacion

class RegistroUsuForm(UserCreationForm):
    username= forms.CharField(label= 'Usuario')
    correo = forms.EmailField()
    direccion = forms.CharField()
    telefono = forms.CharField()
    fecha_nac = forms.DateField(label= 'Fecha de Nacimiento')
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirma Contraseña', widget= forms.PasswordInput)
    class Meta:
        model= User
        fields=('username', 'correo', 'direccion', 'telefono', 'fecha_nac', 'password1', 'password2')
        help_texts= {k:"" for k in fields}

class PublicacionFormB(forms.ModelForm):
    class Meta:
        model= Publicacion
        fields= ('objetivo', 'nombre_pub', 'direccion_pub', 'oferta', 'info_general', 'img')
        exclude= ('img', 'direccion_pub')
        labels= {
            'objetivo': '¿Qué deseas publicar?',
            'nombre_pub': 'Nombre de la Publicación',
            'direccion_pub': 'Dirección del Lugar',
            'oferta': 'Ofreces (CLP)',
            'info_general': 'Información General',
            'img': 'Adjunta tus archivos'
        }

class PublicacionFormC(forms.ModelForm):
    class Meta:
        model= Publicacion
        fields= ('objetivo', 'nombre_pub', 'direccion_pub', 'oferta', 'info_general', 'img')
        labels= {
            'objetivo': '¿Qué deseas publicar?',
            'nombre_pub': 'Nombre de la Publicación',
            'direccion_pub': 'Dirección del Lugar',
            'oferta': 'Costo (CLP)',
            'info_general': 'Información General',
            'img': 'Adjunta tus archivos'
        }