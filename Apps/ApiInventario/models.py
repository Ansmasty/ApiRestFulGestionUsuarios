from django.db import models

# Create your models here.

class Activo(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=100, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])

    def __str__(self):
        return self.nombre