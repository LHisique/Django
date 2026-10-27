from django.contrib import admin
from .models import Categoria, Cidade, Empresa, Contato, Compromisso


class CompromissoInline(admin.TabularInline):
    model = Compromisso
    extra = 0


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Descricao', 'total_contatos')
    search_fields = ('Nome',)

    def total_contatos(self, obj):
        return obj.contatos.count()
    total_contatos.short_description = 'Contatos (1:N)'


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Estado', 'total_empresas')
    search_fields = ('Nome', 'Estado')

    def total_empresas(self, obj):
        return obj.empresas.count()
    total_empresas.short_description = 'Empresas (1:N)'


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'CNPJ', 'Cidade', 'total_contatos')
    search_fields = ('Nome', 'CNPJ')
    list_filter = ('Cidade',)

    def total_contatos(self, obj):
        return obj.contatos.count()
    total_contatos.short_description = 'Contatos (1:N)'


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Email', 'Telefone', 'DtaNas', 'Categoria', 'Empresa')
    search_fields = ('Nome', 'Email')
    list_filter = ('Categoria', 'Empresa')
    inlines = [CompromissoInline]


@admin.register(Compromisso)
class CompromissoAdmin(admin.ModelAdmin):
    list_display = ('id', 'Titulo', 'Contato', 'Data', 'Hora', 'Local')
    search_fields = ('Titulo', 'Contato__Nome', 'Local')
    list_filter = ('Data', 'Contato')
