import itertools

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image

from ckeditor_uploader.fields import RichTextUploadingField


class Project(models.Model):
    """
    Project model definition
    """

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='project/project/%Y/%m/%D',
    )
    description = models.TextField()
    content = RichTextUploadingField()
    date_created = models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name="Starting date"
    )
    date_ended = models.DateField(
        null=True,
        blank=True,
        verbose_name="Termination date"
    )

    class Meta:
        """
        Meta definition for Project.
        """

        ordering = ['-date_created']

    def __str__(self):
        """
        Unicode representation of Project.
        """

        return f"{self.title.capitalize() }"

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
        value = self.title
        slug_result = slug_original = \
            slugify(value, allow_unicode=False)[:max_length]

        for i in itertools.count(1):
            if not Project.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def save(self, *args, **kwargs):
        """
        Save method for Project.

        Generate a slug based on the title if the project doesn't exist yet.-
        """

        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 450 or img.width > 450:
            output_size = (450, 450)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        """
        Return absolute url for Project.
        """

        return reverse('project:project-detail', kwargs={'slug': self.slug})
