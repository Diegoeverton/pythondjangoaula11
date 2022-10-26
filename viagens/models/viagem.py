from django.db import models
from .classe_viagem import ClasseViagem

class Viagem(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_ida = models.DateField()
    data_volta = models.DateField()
    informacoes = models.TextField(max_length=200, blank=True)
    classe_viagem = models.CharField(max_length=4, choices=ClasseViagem.choices, default=0)