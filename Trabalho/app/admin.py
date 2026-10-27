from django.contrib import admin
from .models import Empresa, Contato, Compromisso


class CompromissoInline(admin.TabularInline):
    model = Compromisso
    extra = 0
    exclude = ('Participantes',)


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'CNPJ', 'total_contatos')
    search_fields = ('Nome', 'CNPJ')

    def total_contatos(self, obj):
        return obj.contatos.count()
    total_contatos.short_description = 'Contatos'


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Email', 'Telefone', 'DtaNas', 'Empresa')
    search_fields = ('Nome', 'Email')
    list_filter = ('Empresa',)
    inlines = [CompromissoInline]


@admin.register(Compromisso)
class CompromissoAdmin(admin.ModelAdmin):
    list_display = ('id', 'Titulo', 'Contato', 'Data', 'Hora', 'Local', 'total_participantes')
    search_fields = ('Titulo', 'Contato__Nome', 'Local')
    list_filter = ('Data', 'Contato')
    filter_horizontal = ('Participantes',)

    def total_participantes(self, obj):
        return obj.Participantes.count()
    total_participantes.short_description = 'Participantes'

