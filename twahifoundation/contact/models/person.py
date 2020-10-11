import itertools

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from .company import Company


class Person(models.Model):
    """
    Person model definition
    """

    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(
        max_length=60,)
    last_name = models.CharField(
        max_length=60,)
    email = models.EmailField(max_length=254,)
    phone_number = models.CharField(
        max_length=60, null=True, blank=True)
    is_supplier = models.BooleanField(
        default=False, verbose_name="Is a supplier")
    is_donor = models.BooleanField(
        default=False, verbose_name="Is a donor")
    is_subscribed = models.BooleanField(
        default=False, verbose_name="Is subscribed to the newsletter")
    slug = models.SlugField(max_length=60, unique=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        """
        Meta definition for Person.
        """

        verbose_name = 'Individual'
        verbose_name_plural = 'Individuals'

    def __str__(self):
        """
        Unicode representation of Person.
        """

        return f"{ self.last_name.capitalize() } { self.first_name.capitalize() } | {self.email}"

    def _generate_slug(self):
        """
        Generate a slug based on the firstname and lastname of the person

        If the slug is already taken, one or two digits will be added at the
        end of the slug and will increment as long as the slug already exist
        until reaching a non-existant result.
        The slug is truncated to 57 character in order to add the unique digits
        at the end of it.
        """

        max_length = self._meta.get_field('slug').max_length - 3
        value = f'{self.first_name} {self.last_name}'
        slug_result = slug_original = \
            slugify(value, allow_unicode=False)[:max_length]

        for i in itertools.count(1):
            if not Person.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def get_absolute_url(self):
        "Get the absolute url of the object"
        return reverse("contact:person-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """
        Save method for Person.

        Generate a slug based on the firstname and lastname if the person doesn't exist yet.-
        """

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    def delete_toggle(self):
        """Toggle beetwen the is_deleted field"""

        if self.is_deleted:
            self.is_deleted = False
        else:
            self.is_deleted = True

        self.save()
