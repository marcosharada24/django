from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_lenght=100)
    email = models.EmailField()
    senha = models.CharField(max_length=16)
    