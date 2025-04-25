from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_lenght=100)
    email = models.EmailField()
    senha = models.CharField(max_length=16)

class produto:
     nome = models.CharField(max_lenght=100)
     descricao = models.CharField(max_lenght=500)
     preço = models.CharField(max_lenght=10)
     iamgem = models.ImageField(upload_to='imagens/')
     estoque = models.CharField(max_lenght=10)