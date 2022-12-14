from django.db import models

class BoardGame(models.Model):
    idBoardGame = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=60)
    precio = models.FloatField()
    complejidad = models.CharField(max_length=10)
    descripcion = models.TextField(default="")
    



class Film(models.Model):
    idFilm = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    fecha_estreno = models.DateField()
    pais = models.CharField(max_length=20)
    genero = models.CharField(max_length=50, default="Sin genero")
    sinopsis = models.TextField(default="null")
