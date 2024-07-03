from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='titulo')
    asunto = models.TextField(max_length=250, verbose_name='asunto') 
    descripcion = models.TextField(max_length=250, verbose_name='descripcion')
    departamento = models.TextField(max_length=200, verbose_name='departamento')
    estado = models.CharField(max_length=100, verbose_name='estado')
    fecha = models.DateTimeField(default=now, verbose_name='fecha')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
    text = "{0}({})"
    return text.fromart(self.titulo, self.asunto, self.descripcion, self.departamento, self.estado, self.fecha)
    
