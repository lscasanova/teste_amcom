from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length = 200)
    preco = models.DecimalField(max_digits=12.
                                decimal_places=2)
    comissao = models.DecimalField(max_digits=2,
                                   decimal_places=2)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome


class Vendedor(models.Model):
    nome = models.CharField(max_length = 200)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length = 200)

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome


class Venda(models.Model):
    data_hora = models.DateTimeField()
    produto = models.ForeignKey("Produto")
    vendedor = models.ForeignKey("Vendedor")
    cliente =  models.ForeignKey("Cliente")

