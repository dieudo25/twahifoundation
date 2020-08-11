import itertools

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """
    Category model definition
    """

    class Meta:
        """
        Meta definition for Category.
        """

        verbose_name_plural = 'Categories'
        ordering = ['name']

    name = models.CharField(max_length=100,)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        """
        Unicode representation of Category.
        """

        return f"{self.name}"

    def _generate_slug(self):
        """
        Generate a slug based on the title of the category

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
            if not Category.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def save(self, *args, **kwargs):
        """
        Save method for Category.

        Generate a slug based on the title if the category doesn't exist yet.-
        """

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Return absolute url for Category.
        """

        return reverse('stock:category-list')
