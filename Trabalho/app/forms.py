from django import forms
from .models import Empresa, Contato, Compromisso


class EmpresaModelForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['Nome', 'CNPJ']


class ContatoModelForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['Nome', 'Email', 'Telefone', 'DtaNas', 'Empresa']
        widgets = {
            'DtaNas': forms.DateInput(attrs={'type': 'date'}),
        }


class CompromissoModelForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        fields = ['Titulo', 'Data', 'Hora', 'Local', 'Descricao', 'Contato', 'Participantes']
        widgets = {
            'Data': forms.DateInput(attrs={'type': 'date'}),
            'Hora': forms.TimeInput(attrs={'type': 'time'}),
            'Descricao': forms.Textarea(attrs={'rows': 3}),
            'Participantes': forms.CheckboxSelectMultiple(),
        }

