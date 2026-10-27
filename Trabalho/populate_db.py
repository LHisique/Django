import os
import sys
import django
from datetime import date, time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from app.models import Empresa, Contato, Compromisso


def populate():
    print("Iniciando populacao do banco de dados...")

    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@email.com', 'admin123')
        print("-> Superusuario 'admin' criado.")

    empresas_data = [
        {"Nome": "TechSolutions Brasil", "CNPJ": "12.345.678/0001-90"},
        {"Nome": "Inovação Digital Ltda", "CNPJ": "98.765.432/0001-11"},
        {"Nome": "Nexus Consultoria", "CNPJ": "55.444.333/0001-22"},
        {"Nome": "Alfa Engenharia de Software", "CNPJ": "77.888.999/0001-33"},
    ]
    empresas = {}
    for emp in empresas_data:
        obj, _ = Empresa.objects.get_or_create(Nome=emp["Nome"], defaults=emp)
        empresas[emp["Nome"]] = obj

    contatos_data = [
        {
            "Nome": "Carlos Eduardo Silva",
            "Email": "carlos.silva@techsolutions.com",
            "Telefone": "(11) 98765-4321",
            "DtaNas": date(1990, 5, 12),
            "Empresa": empresas["TechSolutions Brasil"],
        },
        {
            "Nome": "Mariana Ferreira Costa",
            "Email": "mariana.costa@inovacao.com",
            "Telefone": "(19) 97654-3210",
            "DtaNas": date(1995, 8, 23),
            "Empresa": empresas["Inovação Digital Ltda"],
        },
        {
            "Nome": "Lucas Gabriel Isique",
            "Email": "lucas.isique@nexus.com.br",
            "Telefone": "(11) 99988-7766",
            "DtaNas": date(2002, 3, 15),
            "Empresa": empresas["Nexus Consultoria"],
        },
        {
            "Nome": "Beatriz Albuquerque",
            "Email": "beatriz@alfa.com.br",
            "Telefone": "(31) 98888-7777",
            "DtaNas": date(1993, 11, 30),
            "Empresa": empresas["Alfa Engenharia de Software"],
        },
    ]
    contatos = {}
    for ct in contatos_data:
        obj, _ = Contato.objects.get_or_create(Email=ct["Email"], defaults=ct)
        contatos[ct["Nome"]] = obj

    compromissos_data = [
        {
            "Titulo": "Alinhamento do Trabalho de Django",
            "Data": date(2026, 10, 1),
            "Hora": time(14, 0),
            "Local": "Lab de Informática - Faculdade",
            "Descricao": "Revisão do alinhamento do projeto e cronograma de entregas.",
            "Contato": contatos["Lucas Gabriel Isique"],
        },
        {
            "Titulo": "Apresentação de Proposta Comercial",
            "Data": date(2026, 10, 5),
            "Hora": time(10, 30),
            "Local": "Auditório TechSolutions",
            "Descricao": "Apresentação dos módulos e cronograma do sistema.",
            "Contato": contatos["Carlos Eduardo Silva"],
        },
        {
            "Titulo": "Reunião de Parceria Estratégica",
            "Data": date(2026, 10, 10),
            "Hora": time(16, 0),
            "Local": "Google Meet",
            "Descricao": "Discussão de termos de cooperação técnica.",
            "Contato": contatos["Mariana Ferreira Costa"],
        },
    ]

    participantes_data = {
        "Alinhamento do Trabalho de Django": ["Lucas Gabriel Isique", "Mariana Ferreira Costa"],
        "Apresentação de Proposta Comercial": ["Carlos Eduardo Silva", "Lucas Gabriel Isique", "Beatriz Albuquerque"],
        "Reunião de Parceria Estratégica": ["Mariana Ferreira Costa", "Carlos Eduardo Silva"],
    }
    for comp in compromissos_data:
        obj, _ = Compromisso.objects.get_or_create(
            Titulo=comp["Titulo"],
            defaults=comp
        )
        obj.Participantes.set([contatos[n] for n in participantes_data[comp["Titulo"]]])

    print("[SUCESSO] Banco de dados populado com sucesso!")


if __name__ == '__main__':
    populate()

