from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
class Receta(models.Model):
    titulo = models.CharField(max_length=255)
    ingredientes = models.CharField(max_length=255)
    preparacion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    fecha_registro = models.CharField(max_length=255)
    usuario_autor = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Comentario(models.Model):
    texto = models.CharField(max_length = 255)
    receta = models.ForeignKey(Receta,on_delete=models.CASCADE)

