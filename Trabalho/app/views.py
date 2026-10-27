from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Empresa, Contato, Compromisso
from .forms import (
    EmpresaModelForm,
    ContatoModelForm,
    CompromissoModelForm,
)


def index(request):
    lista_contatos = Contato.objects.select_related('Empresa').all()
    lista_empresas = Empresa.objects.all()
    lista_compromissos = Compromisso.objects.select_related('Contato').prefetch_related('Participantes').all()

    context = {
        'lista': lista_contatos,
        'lista_contatos': lista_contatos,
        'lista_empresas': lista_empresas,
        'lista_compromissos': lista_compromissos,
        'total_contatos': lista_contatos.count(),
        'total_empresas': lista_empresas.count(),
        'total_compromissos': lista_compromissos.count(),
    }
    return render(request, "index.html", context)


def consContato(request, pk):
    contato = get_object_or_404(Contato.objects.select_related('Empresa'), id=pk)
    compromissos = contato.compromissos.all()
    participando = contato.compromissos_participando.select_related('Contato').all()
    context = {
        'contato': contato,
        'compromissos': compromissos,
        'participando': participando,
    }
    return render(request, "consultas/consContato.html", context)


def cadContato(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato cadastrado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, "Erro ao cadastrar contato")
    else:
        form = ContatoModelForm()

    return render(request, 'form.html', {'form': form, 'titulo': 'Cadastro de Contato'})


def altContato(request, pk):
    contato = get_object_or_404(Contato, id=pk)
    if request.method == 'POST':
        form = ContatoModelForm(request.POST, request.FILES, instance=contato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contato alterado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao alterar contato')
    else:
        form = ContatoModelForm(instance=contato)

    return render(request, 'form.html', {'form': form, 'titulo': 'Alteração de Contato'})


def excContato(request, pk):
    contato = get_object_or_404(Contato, id=pk)
    if request.method == 'POST':
        contato.delete()
        messages.success(request, 'Contato excluído com sucesso!')
        return redirect('index')

    return render(request, 'excluir.html', {
        'objeto': contato, 'tipo': 'Contato',
        'aviso': 'Os compromissos deste contato também serão excluídos.',
    })


def consEmpresa(request, pk):
    empresa = get_object_or_404(Empresa, id=pk)
    contatos = empresa.contatos.all()
    return render(request, "consultas/consEmpresa.html", {'empresa': empresa, 'contatos': contatos})


def cadEmpresa(request):
    if request.method == 'POST':
        form = EmpresaModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa cadastrada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, "Erro ao cadastrar empresa")
    else:
        form = EmpresaModelForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Cadastro de Empresa'})


def altEmpresa(request, pk):
    empresa = get_object_or_404(Empresa, id=pk)
    if request.method == 'POST':
        form = EmpresaModelForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa alterada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao alterar empresa')
    else:
        form = EmpresaModelForm(instance=empresa)
    return render(request, 'form.html', {'form': form, 'titulo': 'Alteração de Empresa'})


def excEmpresa(request, pk):
    empresa = get_object_or_404(Empresa, id=pk)
    if request.method == 'POST':
        empresa.delete()
        messages.success(request, 'Empresa excluída com sucesso!')
        return redirect('index')
    return render(request, 'excluir.html', {
        'objeto': empresa, 'tipo': 'Empresa',
        'aviso': 'Os contatos desta empresa (e os compromissos deles) também serão excluídos.',
    })


def consCompromisso(request, pk):
    compromisso = get_object_or_404(
        Compromisso.objects.select_related('Contato').prefetch_related('Participantes'), id=pk)
    participantes = compromisso.Participantes.all()
    return render(request, "consultas/consCompromisso.html", {
        'compromisso': compromisso,
        'participantes': participantes,
    })


def cadCompromisso(request):
    if request.method == 'POST':
        form = CompromissoModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compromisso agendado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, "Erro ao agendar compromisso")
    else:
        form = CompromissoModelForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Agendar Compromisso'})


def altCompromisso(request, pk):
    compromisso = get_object_or_404(Compromisso, id=pk)
    if request.method == 'POST':
        form = CompromissoModelForm(request.POST, instance=compromisso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compromisso alterado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao alterar compromisso')
    else:
        form = CompromissoModelForm(instance=compromisso)
    return render(request, 'form.html', {'form': form, 'titulo': 'Alteração de Compromisso'})


def excCompromisso(request, pk):
    compromisso = get_object_or_404(Compromisso, id=pk)
    if request.method == 'POST':
        compromisso.delete()
        messages.success(request, 'Compromisso cancelado com sucesso!')
        return redirect('index')
    return render(request, 'excluir.html', {
        'objeto': compromisso, 'tipo': 'Compromisso',
    })


def relacionamentos(request):
    return render(request, 'relacionamentos.html')

