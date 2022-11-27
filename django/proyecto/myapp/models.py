from django.db import models

class BoardGame(models.Model):
    titulo = models.CharField()
    ##votos_positivos = models.IntegerField()
    precio = models.FloatField()
    ##tematica = models.CharField()
    complejidad = models.CharField()
    ##descripcion = models.TextField()
    




class Film(models.Model):
    titulo = models.CharField()
    director = models.CharField()
    sinopsis = models.TextField()
    fecha_estreno = models.DateField()
    pais = models.CharField()
    ##genero = models.CharField()
