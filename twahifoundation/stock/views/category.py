from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from stock.models.category import Category
from stock.forms.category import CategoryCreateUpdateForm


class CategoryListView(ListView):
    "Category list view"

    model = Category
    template_name = 'stock/category/list.html'
    context_object_name = 'category_list'
    paginate_by = 10


class CategoryListFilteredView(ListView):
    "Category list filterd by title, location"

    model = Category
    template_name = 'stock/category/list.html'
    context_object_name = 'filtered_category_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Category.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


class CategoryUpdateView(UpdateView):
    "Category update view"

    model = Category
    template_name = 'stock/category/update.html'
    context_object_name = 'category'
    form_class = CategoryCreateUpdateForm


class CategoryDeleteView(DeleteView):
    "Category Delete View"

    model = Category
    template_name = 'stock/category/delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('stock:category-list')


class CategoryCreateView(CreateView):
    "Category create view"

    model = Category
    template_name = 'stock/category/create.html'
    form_class = CategoryCreateUpdateForm
