import os
import sys
import django
from datetime import date, time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from app.models import Categoria, Cidade, Empresa, Contato, Compromisso


def populate():
    print("Iniciando população do banco de dados relacional (5 Tabelas)...")

    # 1. Superusuário
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@email.com', 'admin123')
        print("-> Superusuário 'admin' com senha 'admin123' criado com sucesso.")
    else:
        print("-> Superusuário 'admin' já existente.")

    # 2. Cidades (Tabela 2)
    cidades_data = [
        {"Nome": "São Paulo", "Estado": "SP"},
        {"Nome": "Campinas", "Estado": "SP"},
        {"Nome": "Rio de Janeiro", "Estado": "RJ"},
        {"Nome": "Belo Horizonte", "Estado": "MG"},
    ]
    cidades = {}
    for cd in cidades_data:
        obj, _ = Cidade.objects.get_or_create(Nome=cd["Nome"], Estado=cd["Estado"])
        cidades[cd["Nome"]] = obj
    print(f"-> {len(cidades)} Cidades cadastradas.")

    # 3. Categorias (Tabela 1)
    categorias_data = [
        {"Nome": "Clientes", "Descricao": "Clientes ativos de consultoria e serviços"},
        {"Nome": "Fornecedores", "Descricao": "Prestadores de serviços e provedores de infraestrutura"},
        {"Nome": "Parceiros de Negócios", "Descricao": "Empresas e pessoas com acordos de cooperação"},
        {"Nome": "Colegas de Faculdade", "Descricao": "Estudantes da graduação em computação"},
    ]
    categorias = {}
    for cat in categorias_data:
        obj, _ = Categoria.objects.get_or_create(Nome=cat["Nome"], defaults=cat)
        categorias[cat["Nome"]] = obj
    print(f"-> {len(categorias)} Categorias cadastradas.")

    # 4. Empresas (Tabela 3 - N:1 com Cidade)
    empresas_data = [
        {"Nome": "TechSolutions Brasil", "CNPJ": "12.345.678/0001-90", "Cidade": cidades["São Paulo"]},
        {"Nome": "Inovação Digital Ltda", "CNPJ": "98.765.432/0001-11", "Cidade": cidades["Campinas"]},
        {"Nome": "Nexus Consultoria", "CNPJ": "55.444.333/0001-22", "Cidade": cidades["Rio de Janeiro"]},
        {"Nome": "Alfa Engenharia de Software", "CNPJ": "77.888.999/0001-33", "Cidade": cidades["Belo Horizonte"]},
    ]
    empresas = {}
    for emp in empresas_data:
        obj, _ = Empresa.objects.get_or_create(Nome=emp["Nome"], defaults=emp)
        empresas[emp["Nome"]] = obj
    print(f"-> {len(empresas)} Empresas cadastradas.")

    # 5. Contatos (Tabela 4 - N:1 com Categoria e Empresa)
    contatos_data = [
        {
            "Nome": "Carlos Eduardo Silva",
            "Email": "carlos.silva@techsolutions.com",
            "Telefone": "(11) 98765-4321",
            "DtaNas": date(1990, 5, 12),
            "Categoria": categorias["Clientes"],
            "Empresa": empresas["TechSolutions Brasil"],
        },
        {
            "Nome": "Mariana Ferreira Costa",
            "Email": "mariana.costa@inovacao.com",
            "Telefone": "(19) 97654-3210",
            "DtaNas": date(1995, 8, 23),
            "Categoria": categorias["Parceiros de Negócios"],
            "Empresa": empresas["Inovação Digital Ltda"],
        },
        {
            "Nome": "Lucas Gabriel Isique",
            "Email": "lucas.isique@nexus.com.br",
            "Telefone": "(11) 99988-7766",
            "DtaNas": date(2002, 3, 15),
            "Categoria": categorias["Colegas de Faculdade"],
            "Empresa": empresas["Nexus Consultoria"],
        },
        {
            "Nome": "Beatriz Albuquerque",
            "Email": "beatriz@alfa.com.br",
            "Telefone": "(31) 98888-7777",
            "DtaNas": date(1993, 11, 30),
            "Categoria": categorias["Fornecedores"],
            "Empresa": empresas["Alfa Engenharia de Software"],
        },
    ]
    contatos = {}
    for ct in contatos_data:
        obj, _ = Contato.objects.get_or_create(Email=ct["Email"], defaults=ct)
        contatos[ct["Nome"]] = obj
    print(f"-> {len(contatos)} Contatos cadastrados.")

    # 6. Compromissos (Tabela 5 - N:1 com Contato)
    compromissos_data = [
        {
            "Titulo": "Alinhamento do Trabalho de Django",
            "Data": date(2026, 10, 1),
            "Hora": time(14, 0),
            "Local": "Lab de Informática - Faculdade",
            "Descricao": "Revisão dos modelos relacionais 1:N e N:1 para entrega ao Prof. Alexandre Marcelino.",
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
    for comp in compromissos_data:
        Compromisso.objects.get_or_create(
            Titulo=comp["Titulo"],
            Contato=comp["Contato"],
            defaults=comp
        )
    print(f"-> {len(compromissos_data)} Compromissos agendados.")

    print("\n[SUCESSO] Banco de dados populado com 5 tabelas e dados reais!")


if __name__ == '__main__':
    populate()
