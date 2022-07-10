from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views 



urlpatterns = [
    path('homeout/', views.homeout, name='pag-principal'),
    path('', RedirectView.as_view(url= 'homeout/')),
    path('registrarusu', views.registrar, name = 'registrar'),
    path('login', auth_views.LoginView.as_view(template_name= 'appfind/login.html'), name= 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name= 'appfind/logout.html'), name= 'logout'),
    path('frtablero', views.frtablero, name = 'tablero'),
    path('mispublicaciones', views.mispublicaciones, name= 'mis-publicaciones'),
    path('homein', views.homein, name= 'homein'),
    path('formb', views.pubbuscar, name= 'formb'),
    path('formc', views.pubcompartir, name= 'formc')
]