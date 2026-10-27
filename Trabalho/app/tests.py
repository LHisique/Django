from django.test import TestCase, Client
from django.urls import reverse
from datetime import date, time
from .models import Categoria, Cidade, Empresa, Contato, Compromisso


class RelacionamentosTestCase(TestCase):
    def setUp(self):
        # 1. Categoria
        self.categoria = Categoria.objects.create(Nome="Trabalho", Descricao="Contatos profissionais")
        # 2. Cidade
        self.cidade = Cidade.objects.create(Nome="São Paulo", Estado="SP")
        # 3. Empresa (N:1 Cidade)
        self.empresa = Empresa.objects.create(Nome="Tech Corp", CNPJ="11.222.333/0001-44", Cidade=self.cidade)
        # 4. Contato (N:1 Categoria, N:1 Empresa)
        self.contato = Contato.objects.create(
            Nome="Fulano de Tal",
            Email="fulano@teste.com",
            Telefone="11988887777",
            DtaNas=date(1998, 4, 10),
            Categoria=self.categoria,
            Empresa=self.empresa
        )
        # 5. Compromisso (N:1 Contato)
        self.compromisso = Compromisso.objects.create(
            Titulo="Reunião Inicial",
            Data=date.today(),
            Hora=time(10, 0),
            Local="Sala 1",
            Contato=self.contato
        )
        self.client = Client()

    def test_relacionamentos_n_para_1(self):
        """Verifica se chaves estrangeiras apontam corretamente para os registros pais"""
        self.assertEqual(self.empresa.Cidade, self.cidade)
        self.assertEqual(self.contato.Categoria, self.categoria)
        self.assertEqual(self.contato.Empresa, self.empresa)
        self.assertEqual(self.compromisso.Contato, self.contato)

    def test_relacionamentos_1_para_n_reverso(self):
        """Verifica se consultas reversas recuperam os registros filhos"""
        self.assertIn(self.empresa, self.cidade.empresas.all())
        self.assertIn(self.contato, self.categoria.contatos.all())
        self.assertIn(self.contato, self.empresa.contatos.all())
        self.assertIn(self.compromisso, self.contato.compromissos.all())

    def test_rotas_status_code_200(self):
        """Verifica se as páginas principais retornam HTTP 200"""
        rotas = [
            'index',
            'cadContato',
            'cadCategoria',
            'cadCidade',
            'cadEmpresa',
            'cadCompromisso',
            'relacionamentos',
        ]
        for rota in rotas:
            response = self.client.get(reverse(rota))
            self.assertEqual(response.status_code, 200, f"Erro na rota {rota}")

    def test_consulta_contato_detalhes(self):
        """Verifica a página de consulta com o contato e compromissos"""
        response = self.client.get(reverse('consContato', args=[self.contato.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fulano de Tal")
        self.assertContains(response, "Reunião Inicial")
