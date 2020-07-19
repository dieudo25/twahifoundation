from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
        User model definition
    """

    class Meta:
        """
            Meta definition for User.
        """

        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

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
        null=True, blank=True, upload_to='account/user/avatar/%Y/%m/%D')

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
