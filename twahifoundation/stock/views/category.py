from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from account.permissions.group import group_required, GroupRequiredMixin
from stock.models.category import Category
from stock.forms.category import CategoryCreateUpdateForm


class CategoryListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Category list view"

    model = Category
    group_required = [u'Administrator',
                      u'President', u'Stock manager', u'Member']
    template_name = 'stock/category/list.html'
    context_object_name = 'category_list'
    paginate_by = 10


class CategoryListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Category list filterd by title, location"

    model = Category
    group_required = [u'Administrator',
                      u'President', u'Stock manager', u'Member']
    template_name = 'stock/category/list.html'
    context_object_name = 'filtered_category_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Category.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


class CategoryUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Category update view"

    model = Category
    group_required = [u'Administrator', u'President', u'Stock manager', ]
    template_name = 'stock/category/update.html'
    context_object_name = 'category'
    form_class = CategoryCreateUpdateForm


class CategoryDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Category Delete View"

    model = Category
    group_required = [u'Administrator', u'President', u'Stock manager', ]
    template_name = 'stock/category/delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('stock:category-list')


class CategoryCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Category create view"

    model = Category
    group_required = [u'Administrator', u'President', u'Stock manager', ]
    template_name = 'stock/category/create.html'
    form_class = CategoryCreateUpdateForm
