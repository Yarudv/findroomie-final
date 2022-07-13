from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('homeout/', views.homeout, name='pag-principal'),
    path('', RedirectView.as_view(url= 'homeout/')),
    path('registrarusu', views.registrar, name = 'registrar'),
    path('login', LoginView.as_view(template_name= 'appfind/login.html'), name= 'login'),
    path('logout', LogoutView.as_view(template_name= 'appfind/logout.html'), name= 'logout'),
    path('frtablero', views.frtablero, name = 'tablero'),
    path('homein', views.homein, name= 'homein'),
    path('formb', views.pubbuscar, name= 'formb'),
    path('formc', views.pubcompartir, name= 'formc'),
    path('enviop', views.enviop, name= 'enviop'),
    path('mispublicaciones/<int:id>', views.mispublicaciones, name= 'mispublicaciones'),
    path('eliminarpub/<int:id>', views.eliminarpub, name= 'eliminarpub'),
    path('quienessomos', views.quieness, name= 'quienes')
] 