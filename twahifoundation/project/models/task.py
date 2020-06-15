import itertools

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from account.models.user import User
from project.models.project import Project


class Task(models.Model):
    """
    Task model definition
    """

    STATE_CHOICES = [
        ('TODO', 'TO DO'),
        ('PENDING', 'PENDING'),
        ('IN_PROGRESS', 'IN PROGRESS'),
        ('LATE', 'LATE'),
        ('DONE', 'DONE')
    ]

    users = models.ManyToManyField(User, verbose_name="Utilisateur")
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="Projet"
    )
    state = models.CharField(
        max_length=11,
        choices=STATE_CHOICES,
        default=STATE_CHOICES[0][0],
        verbose_name="Statut"
    )
    title = models.CharField(max_length=255, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    date_created = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Date de création"
    )
    deadline = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date limite"
    )

    class Meta:
        """
        Meta definition for Task.
        """

        verbose_name = 'Tâche'
        verbose_name_plural = 'Tâches'
        ordering = ['-date_created']
