from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellidoPaterno = models.CharField(max_length=255)
    apellidoMaterno = models.CharField(max_length=255)
    nombreUsuario = models.CharField(max_length=20)
    email = models.CharField(max_length=25)
    edad = models.IntegerField()
    contrasenia = models.CharField(max_length=32)
    
    def __str__(self):
        return f'Persona {self.id} : {self.nombre} {self.apellidoPaterno} {self.apellidoMaterno} {self.nombreUsuario} {self.email} {self.edad} {self.contrasenia}'


""" class Artista(Persona):
     """