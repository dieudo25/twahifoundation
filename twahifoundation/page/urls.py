from django.urls import re_path

from page.views.page import (
    HomeView,
    AboutView,
    DonateView,
    ContactView,
    ContactSuccessView,
    NewsListView,
    NewsDatailView,
)


from page.views.page import FundRaisingEventListView
from project.views.project import ProjectListView

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

    # Event
    re_path(r'^events/$', FundRaisingEventListView.as_view(), name="event-list"),

    # Post
    re_path(r'^news/$', NewsListView.as_view(), name="news-list"),
    re_path(r'^news/(?P<slug>[a-z0-9-]*)/$',
            NewsDatailView.as_view(), name="news-detail"),


]
