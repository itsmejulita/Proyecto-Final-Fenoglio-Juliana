from django.db import models

# Create your models here.
class Vinoteca(models.Model):
    nombre = models.CharField(max_length=30)
    empresa = models.CharField(max_length= 30)
    año = models.DateField() 


class Cafeteria(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length= 30)
    fecha= models.DateField()

class Heladeria(models.Model):
    nombre = models.CharField(max_length=30)
    producto = models.CharField(max_length= 30)
    cantidad = models.IntegerField()

class Curso(models.Model):
    curso = models.CharField(max_length=30)
    camada = models.IntegerField()