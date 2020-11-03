from django.contrib.sitemaps import Sitemap
from django.db.models import Q
from django.urls import reverse

from blog.models.post import Post
from project.models.event import Event
from project.models.project import Project

class PostSitemap(Sitemap):

    def items(self):
        return Post.objects.filter(
            Q(status='Published') |
            Q(category__name='Page')
        )

class EventSitemap(Sitemap):

    def items(self):
        return Event.objects.filter(status='Published')

class ProjectSitemap(Sitemap):

    def items(self):
        return Project.objects.filter(status='Published')

class StaticViewSitemap(Sitemap):

    def items(self):
        return [
            'page:home',
            'page:donate',
            'page:contact',
        ]

    def location(self, item):
        return reverse(item)