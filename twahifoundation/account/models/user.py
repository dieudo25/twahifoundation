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
    avatar = models.ImageField(null=True, blank=True)
