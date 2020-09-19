from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from account.permissions.group import GroupRequiredMixin
from contact.models.company import Company


class CompanyListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Company list view"

    model = Company
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/company/list.html'
    context_object_name = 'company_list'
    paginate_by = 10


class CompanyListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Company list filterd by email, lastname or firstname"

    model = Company
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/company/list.html'
    context_object_name = 'filtered_company_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Company.objects.filter(
            Q(email__icontains=query) |
            Q(name__icontains=query)
        )
        return object_list


class CompanyDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Company detail view"

    model = Company
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/company/detail.html'
    context_object_name = 'company'


class CompanyUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Company update view"

    model = Company
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/company/update.html'
    context_object_name = 'company'
    fields = [
        'name',
        'email',
        'phone_number',
        'address',
        'website',
        'is_partner',
    ]


class CompanyDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Company Delete View"

    model = Company
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/company/delete.html'
    context_object_name = 'company'
    success_url = reverse_lazy('contact:company-list')


class CompanyCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Company create view"

    model = Company
    group_required = [u'Administrator', u'Member']
    template_name = 'contact/company/create.html'
    fields = [
        'name',
        'email',
        'phone_number',
        'address',
        'website',
        'is_partner',
    ]
