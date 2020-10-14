from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.urls import reverse

from project.models.project import Project
from stock.models.product import Product
from contact.models.person import Person


class Transaction(models.Model):
    """
    Base class of the Transaction model 
    """
    TYPE_CHOICES = [
        ('Donation', 'Donation'),
        ('Purchase', 'Purchase'),
        ('Sell', 'Sell'),
    ]

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
        verbose_name="Responsable",
        null=True,
        blank=True,
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    products_transaction = models.ManyToManyField(
        Product,
        through='ProductTransactionLine',
        blank=True,
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )
    date_time_created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    is_valid = models.BooleanField(default=False)
    with_paypal = models.BooleanField(default=False)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    class Meta:
        """
        Meta definition for Transaction.
        """

        ordering = ['-date_time_created']

    def __str__(self):
        """
        Unicode representation of Transaction.
        """
        transaction_id = str(self.pk)
        add_zero = ''

        while len(add_zero) + len(transaction_id) < 5:
            add_zero += '0'
        return 'T' + add_zero + transaction_id

    def validate(self):
        """
        Validate a transaction, after validation no more modification can be done
        """

        self.is_valid = True
        self.save()


class ProductTransactionLine(models.Model):
    """
    Base class of the ProductTransactionLine model 
    """

    transaction = models.ForeignKey(
        Transaction,
        on_delete=models.CASCADE,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveSmallIntegerField(
        default=None,
    )

    class Meta:
        """
        Meta definition for ProductTransaction.
        """

    @property
    def subtotal(self):
        return self.product.price * self.quantity

    def set_total(self):
        self.transaction.total += self.subtotal

    def save(self, *args, **kwargs):
        """
        Save method for User.

        Generate a slug based on the username if the user doesn't exist yet.-
        """

        if self.transaction.transaction_type != 'Donation':
            self.set_total()

        super().save(*args, **kwargs)
