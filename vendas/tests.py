from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from .models import Produto, Vendedor, Cliente, Venda


class ProdutoTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser("tester", "teste@gmail.com", "123456")
        self.client.login(username="tester", password="123456")
        self.client.force_authenticate(user=self.user)

    def test_inclusao_produto(self):
        url = reverse('produto-list')
        data = {'nome': 'Teste Teste',
                'preco': 123.45,
                'comissao': 5.55}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.count(), 1)
        self.assertEqual(Produto.objects.get().nome, 'Teste Teste')


class VendedorTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser("tester", "teste@gmail.com", "123456")
        self.client.login(username="tester", password="123456")
        self.client.force_authenticate(user=self.user)

    def test_inclusao_vendedor(self):
        url = reverse('vendedor-list')
        data = {'nome': 'Fulano de Tal'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendedor.objects.count(), 1)
        self.assertEqual(Vendedor.objects.get().nome, 'Fulano de Tal')


class ClienteTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser("tester", "teste@gmail.com", "123456")
        self.client.login(username="tester", password="123456")
        self.client.force_authenticate(user=self.user)

    def test_inclusao_cliente(self):
        url = reverse('cliente-list')
        data = {'nome': 'Fulano de Tal'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Cliente.objects.get().nome, 'Fulano de Tal')
