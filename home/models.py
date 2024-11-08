from django.db import models

class Pessoa(models.Model):
    Id = models.AutoField(primary_key=True)
    Nome = models.TextField(max_length=255)
    Email = models.TextField(max_length=255)


class Veiculo(models.Model):
    Id = models.AutoField(primary_key=True)
    NomeVeiculo = models.TextField(max_length=255)
    pessoa = models.OneToOneField(Pessoa, related_name="veiculo", on_delete=models.CASCADE)


class Caminhao(models.Model):
    Id = models.AutoField(primary_key=True)
    Model = models.TextField(max_length=255)

class Caminhoneiro(models.Model):
    Id = models.AutoField(primary_key=True)
    Nome = models.TextField(max_length=200)
    Email = models.TextField(max_length=100)
    Caminhao = models.ForeignKey(Caminhao, on_delete=models.CASCADE, related_name='caminhao')

