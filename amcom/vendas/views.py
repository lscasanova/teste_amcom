from datetime import date, time
from collections import OrderedDict
from operator import itemgetter   

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


from vendas.models import Produto, Vendedor, Cliente, Venda
from vendas.serializers import ProdutoSerializer, VendedorSerializer, ClienteSerializer, VendaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para ver ou editar produtos.
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    @action(methods=['get'], detail=False)
    def produtos_mais_vendidos_por_periodo(self, request, pk=None):
        vendas_no_periodo = Venda.objects.filter(
            data_hora__gte=date.fromisoformat(request.data["data_inicial"]),
            data_hora__lte=date.fromisoformat(request.data["data_final"]))
        produto_quantidade = {}
        for venda in vendas_no_periodo:
            for produto in venda.produto.all():
                produto_quantidade.update({produto.nome: 
                                          produto_quantidade.get(produto.nome, 0)+1})

        produto_quantidade = OrderedDict(sorted(produto_quantidade.items(), key = itemgetter(1), reverse = True))
        return Response(produto_quantidade)


class VendedorViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para ver ou editar vendedores.
    """
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

    @action(methods=['get'], detail=True)
    def comissao_por_periodo(self, request, pk=None):
        vendedor = self.get_object()
        vendas_no_periodo = Venda.objects.filter(
            vendedor=vendedor,
            data_hora__gte=date.fromisoformat(request.data["data_inicial"]),
            data_hora__lte=date.fromisoformat(request.data["data_final"]))
        valor_comissao = 0
        for venda in vendas_no_periodo:
            for produto in venda.produto.all():
                if (venda.data_hora.time() >= time(0, 0)) and (venda.data_hora.time() <= time(12, 0)):
                    comissao = min(produto.comissao, 5)
                else:
                    comissao = max(produto.comissao, 4)
                valor_comissao += (produto.preco * comissao) / 100
        
        return Response({"valor_comissao": valor_comissao})
        

class ClienteViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para ver ou editar clientes.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(methods=['get'], detail=True)
    def produtos_vendidos_por_periodo(self, request, pk=None):
        cliente = self.get_object()
        vendas_no_periodo = Venda.objects.filter(
            cliente=cliente,
            data_hora__gte=date.fromisoformat(request.data["data_inicial"]),
            data_hora__lte=date.fromisoformat(request.data["data_final"]))
        produtos = {}
        for venda in vendas_no_periodo:
            for produto in venda.produto.all():
                produtos.update({produto.id: 
                                          produto.nome})
        return Response(produtos)


class VendaViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para ver ou editar vendas.
    """
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
