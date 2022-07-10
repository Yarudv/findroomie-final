from cProfile import label
from email.policy import default
from random import choices
from django.db import models
from django.forms import CharField

# #class RegistroUsuario(models.Model):
#     rut= models.CharField(max_length= 15)
#     nombre= models.CharField(max_length= 20 )
#     apellido= models.CharField(max_length= 20)
#     usuario= models.CharField(max_length= 15)
#     correo= models.EmailField(max_length= 35)
#     telefono= models.IntegerField(max_length= 15)
#     direccion= models.CharField(max_length= 35)
#     fecha_nacimiento= models.DateField(null= True, blank= True)
#     clave= models.CharField(max_length= 20)
#     confirmar_clave= models.CharField(max_length= 20)

OPCION_OBJETIVO= (
    (True, 'Compartir tu hogar'),
    (False, 'Buscar un lugar')
)

class Publicacion(models.Model):
    objetivo= models.BooleanField(choices= OPCION_OBJETIVO)
    nombre_pub= models.CharField(max_length= 50)
    direccion_pub= models.CharField(max_length= 30)
    fecha_pub= models.DateTimeField(auto_now_add= True)
    oferta= models.IntegerField()
    info_general= models.TextField(max_length= 500)
    img= models.ImageField(upload_to= 'imagenes_publicaciones', default= 'N/A')

