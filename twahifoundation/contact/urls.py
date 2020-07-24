from django.urls import re_path

from contact.views.person import PersonListView, PersonListFiltered

app_name = 'contact'

urlpatterns = [

    # Person CRUD
    re_path(r'^person/list/$', PersonListView.as_view(), name="person-list"),
    re_path(r'^person/list/search/$', PersonListFiltered.as_view(),
            name="person-list-search"),
]
