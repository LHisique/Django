from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Usuario(AbstractUser):
    class Tipo(models.TextChoices):
        ADMINISTRADOR = "ADMINISTRADOR", "Administrador"
        PROFESSOR = "PROFESSOR", "Professor"
        FUNCIONARIO = "FUNCIONARIO", "Funcionario"

    tipo = models.CharField(max_length=15, choices=Tipo.choices, default=Tipo.FUNCIONARIO, verbose_name="Tipo de Usuário")  ## placeholder

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["nome", "usuario"]

    def __str__(self):
        nome = self.get_full_name()
        return nome

    @property
    def is_administrador(self):
        return self.is_superuser or self.tipo == self.Tipo.ADMINISTRADOR

    @property
    def is_professor(self):
        return self.tipo == self.Tipo.PROFESSOR

    @property
    def is_funcionario(self):
        return self.tipo == self.Tipo.FUNCIONARIO


class Ambiente(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name="Nome")  ## cria uma chave de pesquisa (consume mais threads)
    descricao = models.CharField(max_length=150, blank=True, verbose_name="descricao do ambiente")
    capacidade = models.PositiveBigIntegerField(default=1, verbose_name="capacidade do ambiente")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ambiente"
        verbose_name_plural = "Ambientes"
        ordering = ["nome"]

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    ambiente = models.ForeignKey(
        Ambiente,
        on_delete=models.PROTECT,
        related_name="Agendamentos"
        
    )