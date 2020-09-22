from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from account.permissions.group import group_required, GroupRequiredMixin
from stock.models.product import Product
from stock.forms.product import ProductCreateUpdateForm


class ProductListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Product list view"

    model = Product
    group_required = [u'Administrator',
                      u'Stock manager', u'President', u'Member']
    template_name = 'stock/product/list.html'
    context_object_name = 'product_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['product_number'] = Product.objects.all().count()
        return context

    def get_queryset(self):
        object_list = Product.objects.exclude(is_deleted=True)
        return object_list


class ProductListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Product list filterd by title, location"

    model = Product
    group_required = [u'Administrator',
                      u'Stock manager', u'President', u'Member']
    template_name = 'stock/product/list.html'
    context_object_name = 'filtered_product_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)
        ).exclude(is_deleted=True)
        return object_list


class ProductDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Product detail view"

    model = Product
    group_required = [u'Administrator',
                      u'Stock manager', u'President', u'Member']
    template_name = 'stock/product/detail.html'
    context_object_name = 'product'


class ProductUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Product update view"

    model = Product
    group_required = [u'Administrator', u'Stock manager', u'President', ]
    template_name = 'stock/product/update.html'
    context_object_name = 'product'
    form_class = ProductCreateUpdateForm


class ProductDeleteView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Product Delete View"

    model = Product
    group_required = [u'Administrator', u'Stock manager', u'President', ]
    template_name = 'stock/product/delete.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Product create view"

    model = Product
    group_required = [u'Administrator', u'Stock manager', u'President', ]
    template_name = 'stock/product/create.html'
    form_class = ProductCreateUpdateForm


@group_required('Administrator', 'Member')
def delete_restore(request, slug):
    "Change the deleted field of a product"

    product = get_object_or_404(Product, slug=slug)
    product.delete_toggle()
    return redirect(reverse_lazy("stock:product-list"))
