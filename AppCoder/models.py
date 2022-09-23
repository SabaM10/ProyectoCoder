from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=40)
    orientacion = models.CharField(max_length=200)
    def __str__(self):
        return f"Empresa: {self.nombre} - Orientacion: {self.orientacion}"
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    area = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido:{self.apellido} - Email: {self.email} - Area: {self.area} - Empresa: {self.empresa}"

class Administrativo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    area = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido:{self.apellido} - Email: {self.email} - Jefe de Area: {self.area} - Empresa: {self.empresa}"