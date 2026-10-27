from django import forms
from .models import Categoria, Cidade, Empresa, Contato, Compromisso


class CategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['Nome', 'Descricao']


class CidadeModelForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['Nome', 'Estado']


class EmpresaModelForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['Nome', 'CNPJ', 'Cidade']


class ContatoModelForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['Nome', 'Email', 'Telefone', 'DtaNas', 'Categoria', 'Empresa']
        widgets = {
            'DtaNas': forms.DateInput(attrs={'type': 'date'}),
        }


class CompromissoModelForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ['Titulo', 'Data', 'Hora', 'Local', 'Descricao', 'Contato']
        widgets = {
            'Data': forms.DateInput(attrs={'type': 'date'}),
            'Hora': forms.TimeInput(attrs={'type': 'time'}),
            'Descricao': forms.Textarea(attrs={'rows': 3}),
        }
