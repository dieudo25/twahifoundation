import itertools

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Company(models.Model):
    """
    Company model definition
    """

    name = models.CharField(max_length=60, default=None)
    address = models.CharField(
        max_length=60,
        default=None
    )
    email = models.EmailField(max_length=254, default=None)
    phone_number = models.CharField(
        max_length=60,
        null=None
    )
    website = models.URLField(max_length=200, blank=True)
    is_partner = models.BooleanField(
        default=False, verbose_name="Is a partner")
    slug = models.SlugField(max_length=60, unique=True)

    class Meta:
        """
        Meta definition for Company.
        """

        verbose_name_plural = 'Companies'

    def _generate_slug(self):
        """
        Generate a slug based on the name of the company

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
            if not Company.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def __str__(self):
        """
        Unicode representation of Company.
        """

        return f"{self.name}"

    """ def get_absolute_url(self):
        "Get the absolute url of the object"
        return reverse("account:user-detail", kwargs={"slug": self.slug}) """

    def save(self, *args, **kwargs):
        """
        Save method for User.

        Generate a slug based on the username if the user doesn't exist yet.-
        """

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)
