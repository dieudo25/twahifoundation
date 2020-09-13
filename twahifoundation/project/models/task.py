import itertools

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField

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

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="event_created_by")
    slug = models.SlugField(default="slug", max_length=60, unique=True)
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
    description = RichTextUploadingField()
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

        ordering = ['deadline']

    def __str__(self):
        """
        Unicode representation of Task.
        """

        return f"{self.title.capitalize() }"

    def _generate_slug(self):
        """
        Generate a slug based on the title of the task

        If the slug is already taken, one or two digits will be added at the
        end of the slug and will increment as long as the slug already exist
        until reaching a non-existant result.
        The slug is truncated to 57 character in order to add the unique digits
        at the end of it.
        """

        max_length = self._meta.get_field('slug').max_length - 3
        value = self.title
        slug_result = slug_original = \
            slugify(value, allow_unicode=False)[:max_length]

        for i in itertools.count(1):
            if not Task.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def save(self, *args, **kwargs):
        """
        Save method for Task.

        Generate a slug based on the title if the task doesn't exist yet.-
        """

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Return absolute url for ask.
        """

        return reverse('project:task-detail', kwargs={'slug': self.slug})
