from django.urls import re_path

from page.views.page import (
    ContactView,
    ContactSuccessView,
    HomeView,
)
from page.views.donate import (
    DonateView,
    donate_checkout_view,
    DonationSuccesView,
    DonationCancelView,
)
from page.views.page import (
    FundRaisingEventListView,
    ProjectListView,
    PageDetailView,
    NewsListView,
    ProjectDetailView,
    EventDetailView,
    NewsDetailView,
)

app_name = 'page'

urlpatterns = [



    # Static page
    re_path(r'^$', HomeView.as_view(), name="home"),
    re_path(r'^page/(?P<slug>[a-z0-9-]+)/$',
            PageDetailView.as_view(), name="page-detail"),

    # Contact
    re_path(r'^contact/$', ContactView.as_view(), name="contact"),
    re_path(r'^contact/success/$', ContactSuccessView.as_view(),
            name="contact-success"),

    # Donation
    re_path(r'^donate/(?P<pk>[0-9]+)/checkout/$', donate_checkout_view,
            name="donate-checkout"),
    re_path(r'^donate/(?P<pk>[0-9]+)/cancel/$', DonationCancelView.as_view(),
            name="donate-cancel"),
    re_path(r'^donate/(?P<pk>[0-9]+)/success/$', DonationSuccesView.as_view(),
            name="donate-success"),
    re_path(r'^donate/$', DonateView.as_view(), name="donate"),


    # Project
    re_path(r'^projects/$', ProjectListView.as_view(), name="project-list"),
    re_path(r'^projects/(?P<slug>[a-z0-9-]+)/$',
            ProjectDetailView.as_view(), name="project-detail"),

    # Event
    re_path(r'^events/$', FundRaisingEventListView.as_view(), name="event-list"),
    re_path(r'^event/(?P<slug>[a-z0-9-]+)/$',
            EventDetailView.as_view(), name="event-detail"),

    # Post
    re_path(r'^news/$', NewsListView.as_view(), name="news-list"),
    re_path(r'^news/(?P<slug>[a-z0-9-]+)/$',
            NewsDetailView.as_view(), name="news-detail"),

]
