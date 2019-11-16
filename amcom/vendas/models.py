from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length = 200)
    preco = models.DecimalField(max_digits=12,
                                decimal_places=2)
    comissao = models.DecimalField(max_digits=4,
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
    vendedor = models.ForeignKey("Vendedor",
                                 on_delete=models.PROTECT,
                                 blank=True,
                                 null=True)
    cliente =  models.ForeignKey("Cliente",
                                 on_delete=models.PROTECT)
    produto = models.ManyToManyField("Produto")

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)