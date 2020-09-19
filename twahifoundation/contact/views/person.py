from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from account.permissions.group import GroupRequiredMixin
from contact.models.person import Company, Person


class PersonListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Person list view"

    model = Person
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/person/list.html'
    context_object_name = 'person_list'
    paginate_by = 10

    def get_queryset(self):
        current_user = get_user(self.request)
        object_list = Person.objects.filter(created_by=current_user.pk)
        return object_list


class PersonListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Person list filterd by email, lastname or firstname"

    model = Person
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/person/list.html'
    context_object_name = 'filtered_person_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Person.objects.filter(
            Q(email__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
        return object_list


class PersonDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Person detail view"

    model = Person
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/person/detail.html'
    context_object_name = 'person'


class PersonUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Person update view"

    model = Person
    group_required = [u'Administrator', u'Member']
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
        'is_subscribed',
    ]


class PersonDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Person Delete View"

    model = Person
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/person/delete.html'
    context_object_name = 'person'
    success_url = reverse_lazy('contact:person-list')


class PersonCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Person create view"

    model = Person
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/person/create.html'
    fields = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'company',
        'is_supplier',
        'is_donor',
        'is_subscribed',
    ]
