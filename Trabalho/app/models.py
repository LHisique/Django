from django.db import models


class Empresa(models.Model):
    Nome = models.CharField(max_length=100, blank=False, null=False, help_text='Nome da empresa')
    CNPJ = models.CharField(max_length=20, blank=True, null=True, help_text='Informe o CNPJ')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.Nome


class Contato(models.Model):
    Nome = models.CharField(max_length=50, blank=False, null=False, help_text='Informe seu nome')
    Email = models.CharField(max_length=100, blank=False, null=False, help_text='Informe seu e-Mail')
    Telefone = models.CharField(max_length=20, blank=True, null=True, help_text='Informe seu telefone')
    DtaNas = models.DateField(null=True, blank=True, help_text='Informe sua data de nascimento')
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='contatos', help_text='Informe a empresa')

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.Nome


class Compromisso(models.Model):
    Titulo = models.CharField(max_length=100, blank=False, null=False, help_text='Título do compromisso')
    Data = models.DateField(help_text='Data do compromisso')
    Hora = models.TimeField(help_text='Horário do compromisso')
    Local = models.CharField(max_length=100, blank=True, null=True, help_text='Local da reunião')
    Descricao = models.TextField(blank=True, null=True, help_text='Descrição do compromisso')
    Contato = models.ForeignKey(Contato, on_delete=models.CASCADE, related_name='compromissos', help_text='Selecione o contato responsável')
    Participantes = models.ManyToManyField(
        'Contato',
        related_name='compromissos_participando',
        blank=True,
        help_text='Selecione os contatos que participam deste compromisso',
    )

    def __str__(self):
        return f"{self.Titulo} ({self.Contato.Nome})"


