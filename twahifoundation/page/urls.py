from django.urls import re_path

from page.views.page import (
    HomeView,
    AboutView,
    DonateView,
    ContactView,
    ContactSuccessView
)


from project.views.event import EventListView
from project.views.project import ProjectListView

app_name = 'page'

urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name="home"),
    re_path(r'^about/$', AboutView.as_view(), name="about"),
    re_path(r'^contact/$', ContactView.as_view(), name="contact"),
    re_path(r'^contact/success/$', ContactSuccessView.as_view(),
            name="contact-success"),
    re_path(r'^donate/$', DonateView.as_view(), name="donate"),
    re_path(r'^projects/$', ProjectListView.as_view(
        template_name="page/project/list.html"), name="project-list"),
    re_path(r'^events/$', EventListView.as_view(
        template_name="page/event/list.html"), name="event-list"),

    # Paypal

    re_path(r'^checkout/$', HomeView.as_view(), name="home"),
]
