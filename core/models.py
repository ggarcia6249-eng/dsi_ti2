from django.db import models


class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    titulo_academico = models.CharField(max_length=150)
    biografia = models.TextField()
    correo_electronico = models.EmailField()
    dedicacion_persona = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Portfolio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='portfolio/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo