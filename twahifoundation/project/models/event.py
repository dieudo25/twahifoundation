import itertools

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image

from ckeditor_uploader.fields import RichTextUploadingField


from account.models.user import User
from project.models.project import Project


STATUS_CHOICE = (
    ('Drafted', 'Drafted'),
    ('Published', 'Published'),
)

EVENT_TYPE_CHOICES = [
    ('MemberMeeting', 'Meeting between members'),
    ('FundRaising', 'Fund rainsing'),
]


class Event(models.Model):
    """
    Base abstract class of the Event model 
    """

    STATUS_CHOICE = (
        ('Drafted', 'Drafted'),
        ('Published', 'Published'),
    )

    EVENT_TYPE_CHOICES = [
        ('MemberMeeting', 'Meeting between members'),
        ('FundRaising', 'Fund rainsing'),
    ]

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by")
    users = models.ManyToManyField(get_user_model(), blank=True)
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    event_type = models.CharField(
        max_length=14,
        choices=EVENT_TYPE_CHOICES,
        default=EVENT_TYPE_CHOICES[0][0],
    )
    image = models.ImageField(
        upload_to='project/event/%Y/%m/%D',
        default='project/event/event.png'
    )
    content = RichTextUploadingField()
    date_created = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Creation date",
    )
    time_started = models.DateTimeField(
        blank=True,
        verbose_name="Start of the event",
    )
    time_ended = models.DateTimeField(
        blank=True,
        verbose_name="End of the event"
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default='Drafted')

    class Meta:
        """
        Meta definition for Event.
        """

        ordering = ['-date_created']

    def __str__(self):
        """
        Unicode representation of Event.
        """

        return f"{self.title.capitalize() }"

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

        if self.image != None:
            img = Image.open(self.image.path)

            if img.height > 450 or img.width > 450:
                output_size = (450, 450)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def get_absolute_url(self):
        """
        Return absolute url for Event.
        """

        return reverse('project:event-detail', kwargs={'slug': self.slug})

    def status_toggle(self):
        """ Toggle beetwen the status"""

        if self.status == 'Drafted':
            self.status = 'Published'
        else:
            self.status = 'Drafted'

        self.save()
