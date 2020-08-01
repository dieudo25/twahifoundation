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

    users = models.ManyToManyField(User)
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
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Creation date"
    )
    deadline = models.DateField(
        null=True,
        blank=True,
        verbose_name="Deadline date"
    )

    class Meta:
        """
        Meta definition for Task.
        """

        ordering = ['-date_created']
