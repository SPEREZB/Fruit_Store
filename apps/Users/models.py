from django.db import models

# Create your models here.
class Usuarios(models.Model):
    username = models.CharField('Nombre de usuario',unique = True, max_length=100) 
    password = models.CharField('Contaseña',null=False, max_length=10) 
    nombres = models.CharField('Nombres', max_length=200, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length=200,blank = True, null = True) 