from django.urls import path
from .views import (
    index,
    # Contato
    consContato, cadContato, altContato, excContato,
    # Categoria
    consCategoria, cadCategoria, altCategoria, excCategoria,
    # Cidade
    consCidade, cadCidade, altCidade, excCidade,
    # Empresa
    consEmpresa, cadEmpresa, altEmpresa, excEmpresa,
    # Compromisso
    consCompromisso, cadCompromisso, altCompromisso, excCompromisso,
    # Documentação
    relacionamentos,
)

urlpatterns = [
    path('', index, name='index'),

    # Rotas Contato (Tabela Central)
    path('consContato/<int:pk>', consContato, name='consContato'),
    path('cadContato', cadContato, name='cadContato'),
    path('altContato/<int:pk>', altContato, name='altContato'),
    path('excContato/<int:pk>', excContato, name='excContato'),

    # Rotas Categoria (1:N com Contato)
    path('consCategoria/<int:pk>', consCategoria, name='consCategoria'),
    path('cadCategoria', cadCategoria, name='cadCategoria'),
    path('altCategoria/<int:pk>', altCategoria, name='altCategoria'),
    path('excCategoria/<int:pk>', excCategoria, name='excCategoria'),

    # Rotas Cidade (1:N com Empresa)
    path('consCidade/<int:pk>', consCidade, name='consCidade'),
    path('cadCidade', cadCidade, name='cadCidade'),
    path('altCidade/<int:pk>', altCidade, name='altCidade'),
    path('excCidade/<int:pk>', excCidade, name='excCidade'),

    # Rotas Empresa (N:1 com Cidade, 1:N com Contato)
    path('consEmpresa/<int:pk>', consEmpresa, name='consEmpresa'),
    path('cadEmpresa', cadEmpresa, name='cadEmpresa'),
    path('altEmpresa/<int:pk>', altEmpresa, name='altEmpresa'),
    path('excEmpresa/<int:pk>', excEmpresa, name='excEmpresa'),

    # Rotas Compromisso (N:1 com Contato)
    path('consCompromisso/<int:pk>', consCompromisso, name='consCompromisso'),
    path('cadCompromisso', cadCompromisso, name='cadCompromisso'),
    path('altCompromisso/<int:pk>', altCompromisso, name='altCompromisso'),
    path('excCompromisso/<int:pk>', excCompromisso, name='excCompromisso'),

    # Documentação das relações 1:N e N:1
    path('relacionamentos', relacionamentos, name='relacionamentos'),
]
