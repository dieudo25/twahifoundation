from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from stock.models.product import Product
from stock.forms.product import ProductCreateUpdateForm


class ProductListView(ListView):
    "Product list view"

    model = Product
    template_name = 'stock/product/list.html'
    context_object_name = 'product_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['product_number'] = Product.objects.all().count()
        return context


class ProductListFilteredView(ListView):
    "Product list filterd by title, location"

    model = Product
    template_name = 'stock/product/list.html'
    context_object_name = 'filtered_product_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)
        )
        return object_list


class ProductDetailView(DetailView):
    "Product detail view"

    model = Product
    template_name = 'stock/product/detail.html'
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    "Product update view"

    model = Product
    template_name = 'stock/product/update.html'
    context_object_name = 'product'
    form_class = ProductCreateUpdateForm


class ProductDeleteView(DeleteView):
    "Product Delete View"

    model = Product
    template_name = 'stock/product/delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('stock:product-list')


class ProductCreateView(CreateView):
    "Product create view"

    model = Product
    template_name = 'stock/product/create.html'
    form_class = ProductCreateUpdateForm
