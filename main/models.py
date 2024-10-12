from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_nascimento = models.DateField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.nome