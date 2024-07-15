from django.db import models
from django.utils.timezone import now

class Ticket(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    asunto = models.TextField(max_length=100, verbose_name='Asunto')
    descripcion = models.TextField(max_length=200, verbose_name='Descripción')
    departamento = models.CharField(max_length=200, verbose_name='Departamento')
    estado = models.CharField(max_length=200, verbose_name='Estado')
    fecha = models.DateTimeField(default=now, verbose_name='Fecha')
    
    IMPORTANCIA_CHOICES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]
    importancia = models.CharField(max_length=10, choices=IMPORTANCIA_CHOICES, default='media', verbose_name='Importancia')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    def _str_(self):
        return f"{self.titulo} ({self.importancia})"