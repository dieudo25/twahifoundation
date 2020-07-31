from django.urls import re_path

from contact.views.person import (
    PersonDetailView,
    PersonListView,
    PersonListFilteredView,
    PersonUpdateView,
    PersonCreateView,
    PersonDeleteView,
)

app_name = 'contact'

urlpatterns = [

    # Person CRUD
    re_path(r'^person/list/$', PersonListView.as_view(), name="person-list"),
    re_path(r'^person/list/search/$', PersonListFilteredView.as_view(),
            name="person-list-search"),
    re_path(r'^person/create/$', PersonCreateView.as_view(),
            name="person-create"),
    re_path(r'^person/(?P<slug>[a-z0-9-]*)/$',
            PersonDetailView.as_view(), name="person-detail"),
    re_path(r'^person/(?P<slug>[a-z0-9-]*)/update/$',
            PersonUpdateView.as_view(), name="person-update"),

    re_path(r'^person/(?P<slug>[a-z0-9-]*)/delete/$',
            PersonDeleteView.as_view(), name="person-delete"),
]
