import itertools

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from account.models.user import User
from project.models.project import Project


class Event(models.Model):
    """
    Base abstract class of the Event model 
    """

    EVENT_TYPE_CHOICES = [
        ('MemberMeeting', 'Meeting between members'),
        ('FundRainsing', 'Fund rainsing'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, blank=True)
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=255, verbose_name="Titre")
    location = models.CharField(max_length=255, verbose_name="Lieu")
    type = models.CharField(
        max_length=13,
        choices=EVENT_TYPE_CHOICES,
        default=EVENT_TYPE_CHOICES[0][0],
        verbose_name="Type d'évènement"
    )
    image = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="URL de l'image"
    )
    description = models.TextField(verbose_name="Description")
    date_created = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Date de création"
    )
    time_started = models.DateTimeField(
        blank=True,
        verbose_name="Début de l'évènement"
    )
    time_ended = models.DateTimeField(
        blank=True,
        verbose_name="Fin de l'évènement"
    )

    class Meta:
        """
        Meta definition for Event.
        """

        verbose_name = 'Évènement'
        verbose_name_plural = 'Évènements'
        ordering = ['-date_created']

    def __str__(self):
        """
        Unicode representation of Event.
        """

        return f"{self.title}"

    def _generate_slug(self):
        """
        Generate a slug based on the title of the event

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
            if not Event.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def save(self, *args, **kwargs):
        """
        Save method for Event.

        Generate a slug based on the title if the event doesn't exist yet.-
        """

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Return absolute url for Event.
        """

        return reverse('event_detail', kwargs={'slug': self.slug})
