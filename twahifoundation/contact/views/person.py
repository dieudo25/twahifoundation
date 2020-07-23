from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from contact.models.person import Company, Person


class PersonListView(ListView):
    "Person list view"

    model = Person
    template_name = 'contact/person/list.html'
    context_object_name = 'person_list'
