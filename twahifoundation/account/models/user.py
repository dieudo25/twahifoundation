import itertools

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image


class User(AbstractUser):
    """
        User model definition
    """

    class Meta:
        """
            Meta definition for User.
        """

    LANGUAGE_CHOICES = [
        ('FR', 'Français'),
        ('EN', 'English')
    ]

    language = models.CharField(
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default=LANGUAGE_CHOICES[0][0],
        verbose_name="Langue"
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='account/user/avatar/%Y/%m/%D',
        default='account/user/avatar/default.png'
    )

    slug = models.SlugField(max_length=60, unique=True)

    def _generate_slug(self):
        """
        Generate a slug based on the title of the project

        If the slug is already taken, one or two digits will be added at the
        end of the slug and will increment as long as the slug already exist
        until reaching a non-existant result.
        The slug is truncated to 57 character in order to add the unique digits
        at the end of it.
        """

        max_length = self._meta.get_field('slug').max_length - 3
        value = self.username
        slug_result = slug_original = \
            slugify(value, allow_unicode=False)[:max_length]

        for i in itertools.count(1):
            if not User.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def __str__(self):
        """
        Unicode representation of Event.
        """

        return f"{ self.last_name.capitalize() } { self.first_name.capitalize() }"

    def get_absolute_url(self):
        """Get the absolute url of the object"""
        return reverse("user-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """
        Save method for User.

        Generate a slug based on the username if the user doesn't exist yet.-
        """

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

        if self.avatar != None:
            img = Image.open(self.avatar.path)

            if img.height > 250 or img.width > 250:
                output_size = (250, 250)
                img.thumbnail(output_size)
                img.save(self.avatar.path)

    def activate_deactivate(self):
        """Deactivate a user"""

        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True

        self.save()
