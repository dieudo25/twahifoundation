from django.urls import re_path

from page.views.page import (
    HomeView,
    AboutView,
    DonateView,
    ContactView,
    ContactSuccessView,
)

from blog.views.post import PostListView, PostDetailView
from page.views.page import FundRaisingEventListView
from project.views.event import EventDetailView
from project.views.project import ProjectListView, ProjectDetailView

app_name = 'page'

urlpatterns = [

    # Static page
    re_path(r'^$', HomeView.as_view(), name="home"),
    re_path(r'^about/$', AboutView.as_view(), name="about"),
    re_path(r'^contact/$', ContactView.as_view(), name="contact"),
    re_path(r'^contact/success/$', ContactSuccessView.as_view(),
            name="contact-success"),
    re_path(r'^donate/$', DonateView.as_view(), name="donate"),

    # Project
    re_path(r'^projects/$', ProjectListView.as_view(
        template_name="page/project/list.html"), name="project-list"),
    re_path(r'^projects/(?P<slug>[a-z0-9-]*)/$', ProjectDetailView.as_view(
        template_name="page/project/detail.html"), name="project-detail"),

    # Event
    re_path(r'^events/$', FundRaisingEventListView.as_view(), name="event-list"),
    re_path(r'^event/(?P<slug>[a-z0-9-]*)/$', EventDetailView.as_view(
        template_name="page/event/detail.html"), name="event-detail"),

    # Post
    re_path(r'^news/$', PostListView.as_view(
        template_name="page/news/list.html"), name="news-list"),
    re_path(r'^news/(?P<slug>[a-z0-9-]*)/$', PostDetailView.as_view(
        template_name="page/news/detail.html"), name="news-detail"),


]
