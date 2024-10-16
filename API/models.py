from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()
    matricula = models.CharField(max_length=20, unique=True)
    data_matricula = models.DateField(auto_now_add=True)

def __str__(self):
    return self.name

