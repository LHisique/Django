from django.test import TestCase, Client
from django.urls import reverse
from datetime import date, time
from .models import Empresa, Contato, Compromisso


class RelacionamentosTestCase(TestCase):
    def setUp(self):
        self.empresa = Empresa.objects.create(Nome="Tech Corp", CNPJ="11.222.333/0001-44")
        self.contato = Contato.objects.create(
            Nome="Fulano de Tal",
            Email="fulano@teste.com",
            Telefone="11988887777",
            DtaNas=date(1998, 4, 10),
            Empresa=self.empresa
        )
        self.compromisso = Compromisso.objects.create(
            Titulo="Reunião Inicial",
            Data=date.today(),
            Hora=time(10, 0),
            Local="Sala 1",
            Contato=self.contato
        )
        self.contato2 = Contato.objects.create(
            Nome="Ciclano Souza",
            Email="ciclano@teste.com",
            Empresa=self.empresa
        )
        self.compromisso2 = Compromisso.objects.create(
            Titulo="Reunião de Follow-up",
            Data=date.today(),
            Hora=time(15, 0),
            Contato=self.contato2
        )
        self.compromisso.Participantes.set([self.contato, self.contato2])
        self.compromisso2.Participantes.set([self.contato, self.contato2])

        self.client = Client()

    def test_relacionamentos_n_para_1(self):
        self.assertEqual(self.contato.Empresa, self.empresa)
        self.assertEqual(self.compromisso.Contato, self.contato)

    def test_relacionamentos_1_para_n_reverso(self):
        self.assertIn(self.contato, self.empresa.contatos.all())
        self.assertIn(self.compromisso, self.contato.compromissos.all())
        self.assertEqual(self.empresa.contatos.count(), 2)

    def test_rotas_status_code_200(self):
        rotas = [
            'index',
            'cadContato',
            'cadEmpresa',
            'cadCompromisso',
            'relacionamentos',
        ]
        for rota in rotas:
            response = self.client.get(reverse(rota))
            self.assertEqual(response.status_code, 200, f"Erro na rota {rota}")

    def test_consulta_contato_detalhes(self):
        response = self.client.get(reverse('consContato', args=[self.contato.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Fulano de Tal")
        self.assertContains(response, "Reunião Inicial")

    def test_relacionamento_n_para_n(self):
        self.assertEqual(self.compromisso.Participantes.count(), 2)
        self.assertIn(self.contato2, self.compromisso.Participantes.all())
        self.assertEqual(self.contato.compromissos_participando.count(), 2)
        self.assertIn(self.compromisso2, self.contato.compromissos_participando.all())

    def test_n_para_n_independente_da_fk(self):
        self.assertEqual(self.contato2.compromissos.count(), 1)
        self.assertEqual(self.contato2.compromissos_participando.count(), 2)
        self.compromisso.Participantes.remove(self.contato2)
        self.assertEqual(self.compromisso.Participantes.count(), 1)
        self.assertTrue(Compromisso.objects.filter(id=self.compromisso.id).exists())

    def test_consulta_compromisso_mostra_participantes(self):
        response = self.client.get(reverse('consCompromisso', args=[self.compromisso.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ciclano Souza")

        self.assertContains(response, "N:N")
