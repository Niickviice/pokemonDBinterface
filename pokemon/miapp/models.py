from django.db import models

# Create your models here.
class pokemon(models.Model):
    id_pokemon = models.IntegerField()
    peso = models.IntegerField()
    nombre = models.CharField(max_length=50)
    experiencia = models.IntegerField()
