from django.db import models


# Tabela 1: Categoria dos Contatos (Relação 1:N com Contato)
class Categoria(models.Model):
    Nome = models.CharField(max_length=50, blank=False, null=False, help_text='Informe o nome da categoria')
    Descricao = models.CharField(max_length=150, blank=True, null=True, help_text='Informe a descrição')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.Nome


# Tabela 2: Cidade (Relação 1:N com Empresa)
class Cidade(models.Model):
    Nome = models.CharField(max_length=50, blank=False, null=False, help_text='Informe a cidade')
    Estado = models.CharField(max_length=2, blank=False, null=False, help_text='Informe o estado (UF)')

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return f"{self.Nome}/{self.Estado}"


# Tabela 3: Empresa (Relação N:1 com Cidade e 1:N com Contato)
class Empresa(models.Model):
    Nome = models.CharField(max_length=100, blank=False, null=False, help_text='Nome da empresa')
    CNPJ = models.CharField(max_length=20, blank=True, null=True, help_text='Informe o CNPJ')
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='empresas', help_text='Selecione a cidade')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.Nome


# Tabela 4: Contato (Tabela Central do trabalho do Alexandre Marcelino)
# Relacionamento N:1 com Categoria e N:1 com Empresa
# Relacionamento 1:N com Compromisso
class Contato(models.Model):
    Nome = models.CharField(max_length=50, blank=False, null=False, help_text='Informe seu nome')
    Email = models.CharField(max_length=100, blank=False, null=False, help_text='Informe seu e-Mail')
    Telefone = models.CharField(max_length=20, blank=True, null=True, help_text='Informe seu telefone')
    DtaNas = models.DateField(null=True, blank=True, help_text='Informe sua data de nascimento')
    
    # Chaves Estrangeiras (N:1 e 1:N)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='contatos', help_text='Informe a categoria')
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='contatos', help_text='Informe a empresa')

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.Nome


# Tabela 5: Compromisso (Relação N:1 com Contato)
class Compromisso(models.Model):
    Titulo = models.CharField(max_length=100, blank=False, null=False, help_text='Título do compromisso')
    Data = models.DateField(help_text='Data do compromisso')
    Hora = models.TimeField(help_text='Horário do compromisso')
    Local = models.CharField(max_length=100, blank=True, null=True, help_text='Local da reunião')
    Descricao = models.TextField(blank=True, null=True, help_text='Descrição do compromisso')
    
    # Chave Estrangeira (N:1 com Contato)
    Contato = models.ForeignKey(Contato, on_delete=models.CASCADE, related_name='compromissos', help_text='Selecione o contato')

    class Meta:
        verbose_name = 'Compromisso'
        verbose_name_plural = 'Compromissos'

    def __str__(self):
        return f"{self.Titulo} ({self.Contato.Nome})"
