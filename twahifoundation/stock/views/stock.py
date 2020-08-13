from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from stock.models.stock import Stock, ProductStockTransfert
from stock.forms.stock import StockCreateUpdateForm


class StockListView(ListView):
    "Stock list view"

    model = Stock
    template_name = 'stock/stock/list.html'
    context_object_name = 'stock_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['stock_number'] = Stock.objects.all().count()
        return context


class StockListFilteredView(ListView):
    "Stock list filterd by title, location"

    model = Stock
    template_name = 'stock/stock/list.html'
    context_object_name = 'filtered_stock_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Stock.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


class StockDetailReceptionView(DetailView):
    "Stock detail reception view"

    model = Stock
    template_name = 'stock/stock/detail_reception.html'
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['reception'] = ProductStockTransfert.objects.filter(
            stock=self.get_object(),
            transfert_type='RECEPTION'
        )
        return context


class StockDetailDeliveryView(DetailView):
    "Stock detail delivery view"

    model = Stock
    template_name = 'stock/stock/detail_delivery.html'
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['delivry'] = ProductStockTransfert.objects.filter(
            stock=self.get_object(),
            transfert_type='DELIVRY'
        )
        return context


class StockUpdateView(UpdateView):
    "Stock update view"

    model = Stock
    template_name = 'stock/stock/update.html'
    context_object_name = 'stock'
    form_class = StockCreateUpdateForm


class StockDeleteView(DeleteView):
    "Stock Delete View"

    model = Stock
    template_name = 'stock/stock/delete.html'
    context_object_name = 'stock'
    success_url = reverse_lazy('stock:stock-list')


class StockCreateView(CreateView):
    "Stock create view"

    model = Stock
    template_name = 'stock/stock/create.html'
    form_class = StockCreateUpdateForm
