from rest_framework import serializers
from vendas.models import Produto, Vendedor, Cliente, Venda


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "preco", "comissao"]


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ["id", "nome"]


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nome"]


class VendaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ["id", "data_hora", "vendedor", "cliente", "produto"]