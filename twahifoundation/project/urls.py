from django.urls import re_path

from project.views.event import (
    EventListView,
    EventListFilteredView,
    EventDetailView,
    EventUpdateView,
    # EventCreateView,
    # EventDeleteView,
)

app_name = 'project'

urlpatterns = [

    # Event CRUD
    re_path(r'^event/list/$', EventListView.as_view(), name="event-list"),
    re_path(r'^event/list/search/$', EventListFilteredView.as_view(),
            name="event-list-search"),
    # re_path(r'^event/create/$', EventCreateView.as_view(),
    #        name="event-create"),
    re_path(r'^event/(?P<slug>[a-z0-9-]*)/$',
            EventDetailView.as_view(), name="event-detail"),
    re_path(r'^event/(?P<slug>[a-z0-9-]*)/update/$',
            EventUpdateView.as_view(), name="event-update"),
    # re_path(r'^event/(?P<slug>[a-z0-9-]*)/delete/$',
    #        EventDeleteView.as_view(), name="event-delete"),


]
