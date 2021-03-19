from django.db import models

# Create your models here.
class Mensagem(models.Model):
    nome = models.CharField(max_length=100, default="anonimo")
    texto = models.CharField(max_length=100)
