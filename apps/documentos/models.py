from django.db import models
from apps.funcionarios.models import Funcionario

class Documento(models.Model):
    nome = models.CharField(max_length=70)
    pertece = models.ForeignKey(Funcionario, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome