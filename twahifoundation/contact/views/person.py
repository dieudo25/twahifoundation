from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from contact.models.person import Company, Person


class PersonListView(ListView):
    "Person list view"

    model = Person
    template_name = 'contact/person/list.html'
    context_object_name = 'person_list'


class PersonListFilteredView(ListView):
    "Peron list filterd by email, lastname or firstname"

    model = Person
    template_name = 'contact/person/list_filtered.html'
    context_object_name = 'filtered_person_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Person.objects.filter(
            Q(email__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
        return object_list


class PersonDetailView(DetailView):
    "Person detail view"

    model = Person
    template_name = 'contact/person/detail.html'
    context_object_name = 'person'


class PersonUpdateView(UpdateView):
    "Person update view"

    model = Person
    template_name = 'contact/person/update.html'
    context_object_name = 'person'
    fields = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'company',
        'is_supplier',
        'is_donor',
        'is_follower',
    ]
