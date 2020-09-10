from django.urls import re_path
from django.contrib.auth import views as auth_views

from message.views.message import (
    MessageCreateView,
    MessageDeleteView,
)
from message.views.inbox import (
    InboxListView,
    InboxListFilteredView,
    InboxMessageDetailView,
    inbox_to_trash,
)
from message.views.outbox import (
    OutboxListView,
    OutboxListFilteredView,
    OutboxMessageDetailView,
    outbox_to_trash,
)
from message.views.trash import (
    TrashListView,
    TrashListFilteredView,
    TrashMessageDetailView,
    message_restore,
)

app_name = 'message'

urlpatterns = [
    # Message
    re_path(r'^create/$', MessageCreateView.as_view(),
            name="message-create"),
    re_path(r'^(?P<pk>\d+)/delete/$',
            MessageDeleteView.as_view(), name="message-delete"),

    # Inbox
    re_path(r'^inbox/$', InboxListView.as_view(),
            name="inbox"),
    re_path(r'^inbox/search/$', InboxListFilteredView.as_view(),
            name="inbox-search"),
    re_path(r'^inbox/(?P<pk>\d+)/$',
            InboxMessageDetailView.as_view(), name="inbox-detail"),
    re_path(r'^inbox/(?P<pk>\d+)/delete/$',
            inbox_to_trash, name="inbox-delete"),


    # Outbox
    re_path(r'^outbox/$', OutboxListView.as_view(),
            name="outbox"),
    re_path(r'^outbox/search/$', OutboxListFilteredView.as_view(),
            name="outbox-search"),
    re_path(r'^outbox/(?P<pk>\d+)/$',
            OutboxMessageDetailView.as_view(), name="outbox-detail"),
    re_path(r'^outbox/(?P<pk>\d+)/delete/$',
            outbox_to_trash, name="outbox-delete"),

    # Trash
    re_path(r'^trash/$', TrashListView.as_view(),
            name="trash"),
    re_path(r'^trash/search/$', TrashListFilteredView.as_view(),
            name="trash-search"),
    re_path(r'^trash/(?P<pk>\d+)/$',
            TrashMessageDetailView.as_view(), name="trash-detail"),
    re_path(r'^trash/(?P<pk>\d+)/restore/$',
            message_restore, name="trash-restore"),
]
