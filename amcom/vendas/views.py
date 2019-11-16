from rest_framework import viewsets

from vendas.models import Produto, Vendedor, Cliente, Venda
from vendas.serializers import ProdutoSerializer, VendedorSerializer, ClienteSerializer, VendaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para ver ou editar produtos.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para ver ou editar vendedores.
    """
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para ver ou editar clientes.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VendaViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para ver ou editar vendas.
    """
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer