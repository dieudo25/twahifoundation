from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from contact.models.company import Company


class CompanyListView(ListView):
    "Company list view"

    model = Company
    template_name = 'contact/company/list.html'
    context_object_name = 'company_list'


class CompanyListFilteredView(ListView):
    "Company list filterd by email, lastname or firstname"

    model = Company
    template_name = 'contact/company/list.html'
    context_object_name = 'filtered_company_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Company.objects.filter(
            Q(email__icontains=query) |
            Q(name__icontains=query)
        )
        return object_list


class CompanyDetailView(DetailView):
    "Company detail view"

    model = Company
    template_name = 'contact/company/detail.html'
    context_object_name = 'company'


class CompanyUpdateView(UpdateView):
    "Company update view"

    model = Company
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


class CompanyDeleteView(DeleteView):
    "Company Delete View"

    model = Company
    template_name = 'contact/company/delete.html'
    context_object_name = 'company'
    success_url = reverse_lazy('contact:company-list')


class CompanyCreateView(CreateView):
    "Company create view"

    model = Company
    template_name = 'contact/company/create.html'
    fields = [
        'name',
        'email',
        'phone_number',
        'address',
        'website',
        'is_partner',
    ]
