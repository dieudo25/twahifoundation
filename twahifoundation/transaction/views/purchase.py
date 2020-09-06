from django.db.models import Q, Sum
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from transaction.models.transaction import Transaction, ProductTransactionLine
from transaction.forms.purchase import TransactionPurchaseCreateUpdateForm

from transaction.forms.transaction_line import ProductTransactionLineCreateUpdateForm


class TransactionPurchaseListView(ListView):
    "Transaction list view"

    model = Transaction
    template_name = 'transaction/purchase/list.html'
    context_object_name = 'transaction_list'

    def get_queryset(self):
        """Returns Donation that were created today"""

        return Transaction.objects.filter(transaction_type='Purchase')


class TransactionListPurchaseFilteredView(ListView):
    "Transaction list filterd by title, location"

    model = Transaction
    template_name = 'transaction/purchase/list.html'
    context_object_name = 'filtered_transaction_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Transaction.objects.filter(
            Q(user__icontains=query) |
            Q(transaction_type__icontains='Purchase')
        )
        return object_list


class TransactionPurchaseDetailView(DetailView):
    "Transaction detail view"

    model = Transaction
    template_name = 'transaction/purchase/detail.html'
    context_object_name = 'transaction'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['product_transaction_list'] = ProductTransactionLine.objects.filter(
            transaction=self.get_object(),
        )
        transaction_list = ProductTransactionLine.objects.filter(
            transaction=self.get_object(),)
        total = 0
        for line in transaction_list:
            total += line.subtotal
        context['total'] = total
        return context


class TransactionPurchaseUpdateView(UpdateView):
    "Transaction update view"

    model = Transaction
    template_name = 'transaction/purchase/update.html'
    context_object_name = 'transaction'
    form_class = TransactionPurchaseCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:purchase-detail", kwargs={"pk": self.object.pk})


class TransactionPurchaseDeleteView(DeleteView):
    "Transaction Delete View"

    model = Transaction
    template_name = 'transaction/purchase/delete.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('transaction:purchase-list')


class TransactionPurchaseCreateView(CreateView):
    "Transaction create view"

    model = Transaction
    template_name = 'transaction/purchase/create.html'
    form_class = TransactionPurchaseCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:purchase-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):

        form.instance.transaction_type = 'Purchase'
        form.instance.user = self.request.user
        return super(TransactionPurchaseCreateView, self).form_valid(form)


class ProductTransactionPurchaseLineCreateView(CreateView):

    model = ProductTransactionLine
    template_name = 'transaction/product_transaction_line/create.html'
    form_class = ProductTransactionLineCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:purchase-detail", kwargs={"pk": self.object.transaction.pk})

    def form_valid(self, form):
        transaction = Transaction.objects.get(id=self.kwargs['transaction_pk'])
        form.instance.transaction = transaction
        return super(ProductTransactionPurchaseLineCreateView, self).form_valid(form)
