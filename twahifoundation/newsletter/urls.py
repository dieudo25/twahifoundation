from django.urls import re_path

from newsletter.views.newsletter import SubsciberListView, subscribed_add_view


app_name = 'newsletter'

urlpatterns = [
    re_path(r'^subscriber/list$',
            SubsciberListView.as_view(), name="subcriber-list"),
    re_path(r'^subscriber/add$',
            subscribed_add_view, name="subcriber-add"),
]
