from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria, Cidade, Empresa, Contato, Compromisso
from .forms import (
    CategoriaModelForm,
    CidadeModelForm,
    EmpresaModelForm,
    ContatoModelForm,
    CompromissoModelForm,
)


def index(request):
    """Página principal listando os registros e demonstrando as relações do banco"""
    lista_contatos = Contato.objects.select_related('Categoria', 'Empresa').all()
    lista_categorias = Categoria.objects.all()
    lista_cidades = Cidade.objects.all()
    lista_empresas = Empresa.objects.select_related('Cidade').all()
    lista_compromissos = Compromisso.objects.select_related('Contato').all()

    context = {
        'lista': lista_contatos,
        'lista_contatos': lista_contatos,
        'lista_categorias': lista_categorias,
        'lista_cidades': lista_cidades,
        'lista_empresas': lista_empresas,
        'lista_compromissos': lista_compromissos,
        'total_contatos': lista_contatos.count(),
        'total_categorias': lista_categorias.count(),
        'total_cidades': lista_cidades.count(),
        'total_empresas': lista_empresas.count(),
        'total_compromissos': lista_compromissos.count(),
    }
    return render(request, "index.html", context)


# ==========================================
# CRUD CONTATO (Tabela Principal)
# ==========================================
def consContato(request, pk):
    contato = get_object_or_404(Contato.objects.select_related('Categoria', 'Empresa'), id=pk)
    # Relação 1:N -> 1 Contato tem N Compromissos (reverso)
    compromissos = contato.compromissos.all()
    context = {
        'contato': contato,
        'compromissos': compromissos,
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


# ==========================================
# CRUD CATEGORIA (Tabela 1: 1:N com Contato)
# ==========================================
def consCategoria(request, pk):
    categoria = get_object_or_404(Categoria, id=pk)
    contatos = categoria.contatos.all()  # 1:N
    return render(request, "consultas/consCategoria.html", {'categoria': categoria, 'contatos': contatos})


def cadCategoria(request):
    if request.method == 'POST':
        form = CategoriaModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria cadastrada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, "Erro ao cadastrar categoria")
    else:
        form = CategoriaModelForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Cadastro de Categoria'})


def altCategoria(request, pk):
    categoria = get_object_or_404(Categoria, id=pk)
    if request.method == 'POST':
        form = CategoriaModelForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria alterada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao alterar categoria')
    else:
        form = CategoriaModelForm(instance=categoria)
    return render(request, 'form.html', {'form': form, 'titulo': 'Alteração de Categoria'})


def excCategoria(request, pk):
    categoria = get_object_or_404(Categoria, id=pk)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria excluída com sucesso!')
        return redirect('index')
    return render(request, 'excluir.html', {
        'objeto': categoria, 'tipo': 'Categoria',
        'aviso': 'Os contatos desta categoria (e os compromissos deles) também serão excluídos.',
    })


# ==========================================
# CRUD CIDADE (Tabela 2: 1:N com Empresa)
# ==========================================
def consCidade(request, pk):
    cidade = get_object_or_404(Cidade, id=pk)
    empresas = cidade.empresas.all()  # 1:N
    return render(request, "consultas/consCidade.html", {'cidade': cidade, 'empresas': empresas})


def cadCidade(request):
    if request.method == 'POST':
        form = CidadeModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cidade cadastrada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, "Erro ao cadastrar cidade")
    else:
        form = CidadeModelForm()
    return render(request, 'form.html', {'form': form, 'titulo': 'Cadastro de Cidade'})


def altCidade(request, pk):
    cidade = get_object_or_404(Cidade, id=pk)
    if request.method == 'POST':
        form = CidadeModelForm(request.POST, instance=cidade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cidade alterada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao alterar cidade')
    else:
        form = CidadeModelForm(instance=cidade)
    return render(request, 'form.html', {'form': form, 'titulo': 'Alteração de Cidade'})


def excCidade(request, pk):
    cidade = get_object_or_404(Cidade, id=pk)
    if request.method == 'POST':
        cidade.delete()
        messages.success(request, 'Cidade excluída com sucesso!')
        return redirect('index')
    return render(request, 'excluir.html', {
        'objeto': cidade, 'tipo': 'Cidade',
        'aviso': 'As empresas desta cidade (e seus contatos e compromissos) também serão excluídas.',
    })


# ==========================================
# CRUD EMPRESA (Tabela 3: N:1 com Cidade, 1:N com Contato)
# ==========================================
def consEmpresa(request, pk):
    empresa = get_object_or_404(Empresa.objects.select_related('Cidade'), id=pk)
    contatos = empresa.contatos.all()  # 1:N
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


# ==========================================
# CRUD COMPROMISSO (Tabela 5: N:1 com Contato)
# ==========================================
def consCompromisso(request, pk):
    compromisso = get_object_or_404(Compromisso.objects.select_related('Contato'), id=pk)
    return render(request, "consultas/consCompromisso.html", {'compromisso': compromisso})


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
    """Página didática explicando os relacionamentos 1:N e N:1"""
    return render(request, 'relacionamentos.html')
