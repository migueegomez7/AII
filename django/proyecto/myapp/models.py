from django.db import models

class BoardGame(models.Model):
    idBoardGame = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=60)
    ##votos_positivos = models.IntegerField()
    precio = models.FloatField()
    ##tematica = models.CharField()
    complejidad = models.CharField(max_length=10)
    ##descripcion = models.TextField()
    




class Film(models.Model):
    idFilm = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    #sinopsis = models.TextField()
    fecha_estreno = models.DateField()
    pais = models.CharField(max_length=20)
    ##genero = models.CharField()
