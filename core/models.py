from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=250)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nome