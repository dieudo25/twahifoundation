from django.urls import path, include

from contact.views.person import PersonListView

app_name = 'contact'

urlpatterns = [

    # Person CRUD
    path('person/list/', PersonListView.as_view(), name="person-list"),

]
