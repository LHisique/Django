from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contato
from .forms import ContatoModelForm

def index(request):
    lista = Contato.objects.all()
    print(lista)
    context = {
        'lista': lista
    }
    return render(request, "index.html", context)

def consContato(request, pk):
    contato = Contato.objects.get(id = pk)
    context = {
        'contato': contato
    }
    return render(request, "consContato.html", context)

def cadContato(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)

        if form.is_valid():
            contato = form.save()

            messages.success(request, 'Contato cadastrado com sucesso!')
            form = ContatoModelForm()
        else:
            messages.error(request, "Erro ao cadastrar contato")
    else:
        form = ContatoModelForm()

    context = {
        'form': form
    }

    return render(request, 'cadContato.html', context)

def altContato(request, pk):
    contato = Contato.objects.get(id=pk)

    if request.method == 'POST':
        form = ContatoModelForm(request.POST, instance=contato)

        if form.is_valid():
            form.save()
            messages.success(request, 'Contato alterado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, "Erro ao alterar contato")
    else:
        form = ContatoModelForm(instance=contato)

    context = {
        'form': form
    }

    return render(request, 'cadContato.html', context)

def delContato(request, pk):
    contato = Contato.objects.get(id=pk)
    contato.delete()
    messages.success(request, 'Contato excluído com sucesso!')
    return redirect('index')