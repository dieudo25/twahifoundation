import itertools

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image

from blog.models.category import Category
from blog.models.tags import Tags

from ckeditor_uploader.fields import RichTextUploadingField


STATUS_CHOICE = (
    ('Drafted', 'Drafted'),
    ('Published', 'Published'),
)


class Post(models.Model):
    title = models.CharField(max_length=100, )
    slug = models.SlugField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    meta_description = models.TextField(max_length=160, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='updated_by', null=True, blank=True)
    description = models.TextField()
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(
        Tags, related_name='rel_posts', blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default='Drafted')
    keywords = models.TextField(max_length=500, blank=True)
    image = models.ImageField(
        upload_to='blog/post/%Y/%m/%D',
        default='blog/post/post.png'
    )

    class Meta:
        ordering = ['-updated_on']

    def save(self, *args, **kwargs):
        """
        Save method for Post.

        Generate a slug based on the title if the post doesn't exist yet.-
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

    def __str__(self):
        return self.title

    def is_deletable_by(self, user):
        if self.user == user or user.is_superuser:
            return True
        return False

    def _generate_slug(self):
        """
        Generate a slug based on the title of the post

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
            if not Post.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def get_absolute_url(self):
        """Get the absolute url of the object"""
        return reverse("blog:post-detail", kwargs={"slug": self.slug})

    def status_toggle(self):
        """ Toggle beetwen the status"""

        if self.status == 'Drafted':
            self.status = 'Published'
        else:
            self.status = 'Drafted'

        self.save()
