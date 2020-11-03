from django.contrib.sitemaps import Sitemap
from django.db.models import Q
from django.urls import reverse

from blog.models.post import Post
from project.models.event import Event
from project.models.project import Project

class PostSitemap(Sitemap):

    changefreq = "monthly"
    priority = 0.5
    protocol = "https"


    def items(self):
        return Post.objects.filter(
            Q(status='Published') |
            Q(category__name='Page')
        )
    
    def lastmod(self, obj):
        if obj.updated_on:
            return obj.updated_on
        else:
            return obj.created_on


class EventSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return Event.objects.filter(status='Published')

    def lastmod(self, obj):
        return obj.date_created

class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = "https"   

    def items(self):
        return Project.objects.filter(status='Published')
    
    def lastmod(self, obj):
        return obj.date_created

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5
    protocol = "https"   

    def items(self):
        return [
            'page:home',
            'page:donate',
            'page:contact',
        ]

    def location(self, item):
        return reverse(item)