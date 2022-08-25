from django.db import models

# Create your models here.

class Instrumento(models.Model):
    marca = models.CharField(max_length= 20)
    modelo = models.CharField(max_length = 25)
    tipoinstrumento = models.CharField(max_length = 20)
    color = models.CharField (max_length = 15)
    
    def __str__(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Tipo de Instrumento:{self.tipoinstrumento} - Color: {self.color}"
    
class Pedal(models.Model):
    nombre = models.CharField (max_length = 25)
    efecto = models.CharField (max_length = 15)
    bypass = models.BooleanField ()

class Discos(models.Model):
    artista = models.CharField (max_length = 35)
    album = models.CharField (max_length = 35)
    fechaLanzamiento = models.DateField()
    
    def __str__(self):
        return f"Artista: {self.artista} - Album: {self.album} - Fecha de Lanzamiento:{self.fechaLanzamiento}"
    