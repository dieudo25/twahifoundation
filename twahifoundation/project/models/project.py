import itertools

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):
    """
    Project model definition
    """

    slug = models.SlugField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    image = models.URLField(max_length=255, null=True, blank=True,
                            verbose_name="Image URL")
    description = models.TextField()
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

        return f"{self.title}"

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

    def get_absolute_url(self):
        """
        Return absolute url for Project.
        """

        return reverse('project_detail', kwargs={'slug': self.slug})
