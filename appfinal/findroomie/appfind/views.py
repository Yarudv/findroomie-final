import folium
from django.shortcuts import redirect, render
from . models import Publicacion
from django.contrib.auth.models import User
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
            form.instance.user = request.user 
            provee= form.save(commit = False)
            provee.save()
    form= PublicacionFormB()
    return render(request, 'appfind/buscarform.html', {"form": form})

def pubcompartir(request):
    if request.method == "POST":
        form= PublicacionFormC(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user 
            provee= form.save(commit = False)
            print(request.FILES.get("img"))
            provee.img= request.FILES.get("img")
            provee.save()
    form= PublicacionFormC()
    return render(request, 'appfind/compartirform.html', {"form":form})

def frtablero(request):
    popuptext="Santiago de chile"
    santiago= folium.Map(location= [-33.45694, -70.64827], zoom_start= 12)
    folium.Marker(location= [-33.45694, -70.64827], popup= popuptext).add_to(santiago)
    folium.Circle(location= [-33.45694, -70.64827], color= "blue", fill_color= "black", radius= 40, weight= 6, fill_opacity= 0.6).add_to(santiago)
    santiago= santiago._repr_html_()
    bus= Publicacion.objects.filter(objetivo= 'False')
    co= Publicacion.objects.filter(objetivo= 'True')
    return render(request, 'appfind/tablero.html', {'map': santiago, 'bus': bus, 'co': co})

def eliminarpub(request, id):
    usuarioeli = Publicacion.objects.filter(pk= id)
    usuarioeli.delete()
    return render(request, 'appfind/eliminarpub.html')

@login_required
def enviop(request):
    return render(request, 'appfind/enviop.html')

@login_required
def mispublicaciones(request, id):
    usu_pub= Publicacion.objects.filter(user_id = id)
    return render(request, 'appfind/mispublicaciones.html', {'usu_pub': usu_pub})

@login_required
def homein(request):
    return render(request, 'appfind/homein.html')

def quieness(request):
    return render(request, 'appfind/quienessomos.html')










