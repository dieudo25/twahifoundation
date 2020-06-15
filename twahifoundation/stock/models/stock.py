from django.db import models

from stock.models.product import Product


class Stock(models.Model):
    """
    Stock model definition
    """

    name = models.CharField(max_length=100, verbose_name="Nom", default=None)
    location = models.CharField(
        max_length=255,
        verbose_name="Lieu",
        null=True
    )
    products = models.ManyToManyField(
        Product,
        through='ProductStock',
    )
    date_created = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Date de création"
    )
    is_full = models.BooleanField(default=False, verbose_name="Est rempli")

    class Meta:
        """
        Meta definition for Stock.
        """

        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        ordering = ['-date_created']


class ProductStock(models.Model):
    """
    ProductStock model definition
    """

    TYPE_CHOICES = [
        ('RECEPTION', 'Réception'),
        ('RECEPTION', 'Livraison'),
    ]

    stock = models.ForeignKey(
        Stock,
        on_delete=models.PROTECT,
        null=True
    )
    transfert_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[0][0],
        verbose_name="Type de transfert"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        verbose_name="Produits"
    )
    quantity = models.PositiveSmallIntegerField(
        default=None,
        verbose_name="Quantité"
    )
    transfert_date = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Date"
    )

    class Meta:
        """
        Meta definition for ProductStock.
        """

        verbose_name = 'Transfert de produits'
        verbose_name_plural = 'Transferts de produits'
