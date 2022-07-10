import folium
from django.shortcuts import redirect, render
from . models import Publicacion
from .forms import PublicacionFormB, PublicacionFormC, RegistroUsuForm
from django.contrib import messages
from folium.plugins import MiniMap
from django.contrib.auth.decorators import login_required

def homeout(request):
    return render (request, 'appfind/homeout.html')

def registrar(request):
    if request.method == 'POST':
        form= RegistroUsuForm(data= request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con exito')
            return redirect("homeout/")
    else:
        form= RegistroUsuForm()
    context = {'form': form}
    return render(request, 'appfind/usuregistro.html', context)

def pubbuscar(request):
    if request.method == "POST":
        form= PublicacionFormB(data = request.POST)
        if form.is_valid():
            provee= form.save(commit = False)
            provee.save()
            return redirect(request, 'appfind/tablero.html')
    form= PublicacionFormB()
    return render(request, 'appfind/buscarform.html', {"form": form})

def pubcompartir(request):
    if request.method == "POST":
        form= PublicacionFormC(data = request.POST)
        if form.is_valid():
            provee= form.save(commit = False)
            provee.save()
            return redirect(request, 'appfind/tablero.html')
    form= PublicacionFormC()
    return render(request, 'appfind/compartirform.html', {"form":form})

def frtablero(request):
    popuptext="Santiago de chile"
    santiago= folium.Map(location= [-33.45694, -70.64827], zoom_start= 12)
    folium.Marker(location= [-33.45694, -70.64827], popup= popuptext).add_to(santiago)
    folium.Circle(location= [-33.45694, -70.64827], color= "blue", fill_color= "black", radius= 40, weight= 6, fill_opacity= 0.6).add_to(santiago)
    santiago= santiago._repr_html_()
    bus= Publicacion.objects.all()
    comp= Publicacion.objects.all()
    return render(request, 'appfind/tablero.html', {'map': santiago, 'bus': bus, 'comp': comp})

@login_required
def mispublicaciones(request):
    return render(request, 'appfind/mispublicaciones.html')

@login_required
def homein(request):
    return render(request, 'appfind/homein.html')








