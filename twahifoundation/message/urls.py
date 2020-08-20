from django.urls import re_path
from django.contrib.auth import views as auth_views

from message.views.message import (
    MessageCreateView,
    MessageDetailView,
    MessageDeleteView,
    MessageSendListView,
    MessageSendListFilteredView,
    MessageReceivedListView,
    MessageReceivedListFilteredView,
    MessageUpdateView,
)

app_name = 'message'

urlpatterns = [
    re_path(r'^outbox/$', MessageSendListView.as_view(),
            name="message-outbox"),
    re_path(r'^outbox/search/$', MessageSendListFilteredView.as_view(),
            name="message-outbox-search"),
    re_path(r'^inbox/$', MessageReceivedListView.as_view(),
            name="message-inbox"),
    re_path(r'^inbox/search/$', MessageReceivedListFilteredView.as_view(),
            name="message-inbox-search"),
    re_path(r'^create/$', MessageCreateView.as_view(),
            name="message-create"),
    re_path(r'^(?P<pk>\d+)/$',
            MessageDetailView.as_view(), name="message-detail"),
    re_path(r'^(?P<pk>\d+)/update/$',
            MessageUpdateView.as_view(), name="message-update"),

    re_path(r'^(?P<pk>\d+)/delete/$',
            MessageDeleteView.as_view(), name="message-delete"),
]
