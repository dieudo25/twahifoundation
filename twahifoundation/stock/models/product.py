import itertools

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from stock.models.category import Category


class Product(models.Model):
    """
    Product model definition
    """

    class Meta:
        """
        Meta definition for DonnatingTransaction.
        """

        ordering = ['name']

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100,)
    price = models.DecimalField(
        max_digits=20, decimal_places=2,)
    image = models.URLField(
        max_length=255,
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    date_created = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Creation date"
    )
    is_saleable = models.BooleanField(default=True,)
    is_purchasable = models.BooleanField(default=True,)
    is_deleted = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Unicode representation of Product.
        """

        return f"{self.name.capitalize() }"

    def _generate_slug(self):
        """
        Generate a slug based on the title of the product

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
            if not Product.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def save(self, *args, **kwargs):
        """
        Save method for Product.

        Generate a slug based on the title if the product doesn't exist yet.-
        """

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Return absolute url for Product.
        """

        return reverse('stock:product-detail', kwargs={'slug': self.slug})

    def delete_toggle(self):
        """Toggle beetwen the is_deleted field"""

        if self.is_deleted:
            self.is_deleted = False
        else:
            self.is_deleted = True

        self.save()
