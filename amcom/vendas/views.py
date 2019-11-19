from datetime import date, time

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


from vendas.models import Produto, Vendedor, Cliente, Venda
from vendas.serializers import ProdutoSerializer, VendedorSerializer, ClienteSerializer, VendaSerializer, ComissaoSerializer


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
    comissao_serializer = ComissaoSerializer

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


class VendaViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para ver ou editar vendas.
    """
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
