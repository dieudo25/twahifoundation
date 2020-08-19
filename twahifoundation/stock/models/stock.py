import itertools

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from stock.models.product import Product


class Stock(models.Model):
    """
    Stock model definition
    """

    name = models.CharField(max_length=100, default=None)
    slug = models.SlugField(max_length=100, unique=True)
    location = models.CharField(
        max_length=255,
        null=True
    )
    products_transfert = models.ManyToManyField(
        Product,
        through='ProductStockTransfert',
    )
    date_created = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Date de création"
    )
    is_full = models.BooleanField(default=False)

    class Meta:
        """
        Meta definition for Stock.
        """

        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        ordering = ['-date_created']

    def __str__(self):
        """
        Unicode representation of Stock.
        """

        return f"{self.name.capitalize() }"

    def _generate_slug(self):
        """
        Generate a slug based on the title of the stock

        If the slug is already taken, one or two digits will be added at the
        end of the slug and will increment as long as the slug already exist
        until reaching a non-existant result.
        The slug is truncated to 57 character in order to add the unique digits
        at the end of it.
        """

        max_length = self._meta.get_field('slug').max_length - 3
        value = self.name
        slug_result = slug_original = \
            slugify(value, allow_unicode=False)[:max_length]

        for i in itertools.count(1):
            if not Stock.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def save(self, *args, **kwargs):
        """
        Save method for Stock.

        Generate a slug based on the title if the stock doesn't exist yet.-
        """

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Return absolute url for Stock.
        """

        return reverse('stock:stock-reception-detail', kwargs={'slug': self.slug})


class ProductStockTransfert(models.Model):
    """
    StockStock model definition
    """

    TYPE_CHOICES = [
        ('RECEPTION', 'Reception'),
        ('DELIVRY', 'Delivry'),
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
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )
    quantity = models.PositiveSmallIntegerField(
        default=None,
    )
    date_time_created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    class Meta:
        """
        Meta definition for StockStock.
        """

        verbose_name = 'Transfert de produits'
        verbose_name_plural = 'Transferts de produits'

    def __str__(self):
        """
        Unicode representation of Stock.
        """

        stock_transfert_id = str(self.pk)
        add_zero = ''

        while len(add_zero) < 5:
            add_zero += '0'
        return 'ST' + add_zero + stock_transfert_id

    def getstock(self):
        return self.stock_slug

    def get_absolute_url(self):
        """
        Return absolute url for ProductStockStock.
        """

        return reverse('stock:stock-reception-detail', kwargs={'slug': self.request.META.get('HTTP_REFERER')})
