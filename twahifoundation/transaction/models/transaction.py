from django.db import models
from django.conf import settings

from project.models.project import Project
from stock.models.product import Product
from contact.models.person import Donor, Supplier


class Transaction(models.Model):
    """
    Base class of the Transaction model 
    """

    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Projet'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        limit_choices_to={'is_staff': True},
        verbose_name="Responsable"
    )
    donor = models.ForeignKey(
        Donor,
        on_delete=models.PROTECT,
        verbose_name="Donateur",
        blank=True,
        null='NO DONOR',
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        verbose_name="Fournisseur",
        blank=True,
        null='NO SUPPLIER'
    )
    products = models.ManyToManyField(
        Product,
        through='ProductTransactionLine',
        verbose_name="Liste de produits",
        blank=True,
        null='NO PRODUCT'
    )
    date_created = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Date de création"
    )
    is_valid = models.BooleanField(default=False, verbose_name="Est valide")

    class Meta:
        """
        Meta definition for Transaction.
        """

        verbose_name = 'Achat'
        verbose_name_plural = 'Achats'
        ordering = ['-date_created']

    def __str__(self):
        """
        Unicode representation of Transaction.
        """
        transaction_id = str(self.pk)
        add_zero = ''

        while len(add_zero) < 5:
            add_zero += '0'
        return 'T' + add_zero + transaction_id

    def save(self, *args, **kwargs):
        """
        Save method for Transaction.
        """

        super().save(*args, **kwargs)


class ProductTransactionLine(models.Model):

    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.PROTECT,
        null=True
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

    class Meta:
        """
        Meta definition for ProductPurchasingTransaction.
        """

        verbose_name = 'Ligne de commande'
        verbose_name_plural = 'Ligne de commandes'
