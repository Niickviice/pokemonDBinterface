from django.db import models

# Create your models here.
class pokemon(models.Model):
    id_pokemon = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    experiencia = models.CharField(max_length=50)