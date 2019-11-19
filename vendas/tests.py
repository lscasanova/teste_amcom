from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Produto


class ProdutoTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user("tester", "teste@gmail.com", "123456")

    def test_inclusao_produto(self):
        url = reverse('produto-list')
        data = {'nome': 'Teste Teste',
                'preco': 123.45,
                'comissao': 5.55}
        client = APIClient()
        client.login(username="tester", password="123456")
        print(self.user.username)
        response = client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Produto.objects.count(), 1)
        self.assertEqual(Produto.objects.get().name, 'Teste Teste')
