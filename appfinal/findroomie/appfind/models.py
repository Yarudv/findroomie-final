from cProfile import label
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

OPCION_OBJETIVO= (
    (True, 'Compartir tu hogar'),
    (False, 'Buscar un lugar')
)

class Publicacion(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    objetivo= models.BooleanField(choices= OPCION_OBJETIVO)
    nombre_pub= models.CharField(max_length= 50)
    direccion_pub= models.CharField(max_length= 30)
    fecha_pub= models.DateTimeField(auto_now_add=True)
    oferta= models.IntegerField()
    info_general= models.TextField(max_length= 500)
    img= models.ImageField(upload_to= 'imagenes_publicaciones', default= 'template.jpg')


