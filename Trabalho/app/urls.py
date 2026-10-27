from django.urls import path
from .views import (
    index,
    consContato, cadContato, altContato, excContato,
    consEmpresa, cadEmpresa, altEmpresa, excEmpresa,
    consCompromisso, cadCompromisso, altCompromisso, excCompromisso,
    relacionamentos,
)

urlpatterns = [
    path('', index, name='index'),

    path('consContato/<int:pk>', consContato, name='consContato'),
    path('cadContato', cadContato, name='cadContato'),
    path('altContato/<int:pk>', altContato, name='altContato'),
    path('excContato/<int:pk>', excContato, name='excContato'),

    path('consEmpresa/<int:pk>', consEmpresa, name='consEmpresa'),
    path('cadEmpresa', cadEmpresa, name='cadEmpresa'),
    path('altEmpresa/<int:pk>', altEmpresa, name='altEmpresa'),
    path('excEmpresa/<int:pk>', excEmpresa, name='excEmpresa'),

    path('consCompromisso/<int:pk>', consCompromisso, name='consCompromisso'),
    path('cadCompromisso', cadCompromisso, name='cadCompromisso'),
    path('altCompromisso/<int:pk>', altCompromisso, name='altCompromisso'),
    path('excCompromisso/<int:pk>', excCompromisso, name='excCompromisso'),

    path('relacionamentos', relacionamentos, name='relacionamentos'),
]

