from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from transaction.models.transaction import Transaction
from transaction.forms.transaction import TransactionDonationCreateUpdateForm


class TransactionDonationListView(ListView):
    "Transaction list view"

    model = Transaction
    template_name = 'transaction/donation_list.html'
    context_object_name = 'transaction_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['transaction_number'] = Transaction.objects.all().count()
        return context

    def get_queryset(self):
        """Returns Donation that were created today"""

        return Transaction.objects.filter(transaction_type='Donation')


class TransactionListDonationFilteredView(ListView):
    "Transaction list filterd by title, location"

    model = Transaction
    template_name = 'transaction/donation_list.html'
    context_object_name = 'filtered_transaction_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Transaction.objects.filter(
            Q(user__icontains=query) |
            Q(transaction_type__icontains='Donation')
        )
        return object_list


class TransactionSaleListView(ListView):
    "Transaction list view"

    model = Transaction
    template_name = 'transaction/sale_list.html'
    context_object_name = 'transaction_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['transaction_number'] = Transaction.objects.all().count()
        return context

    def get_queryset(self):
        """Returns Donation that were created today"""

        return Transaction.objects.filter(transaction_type='Sell')


class TransactionListSaleFilteredView(ListView):
    "Transaction list filterd by title, location"

    model = Transaction
    template_name = 'transaction/sale_list.html'
    context_object_name = 'filtered_transaction_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Transaction.objects.filter(
            Q(user__icontains=query) |
            Q(transaction_type__icontains='Sell')
        )
        return object_list


class TransactionPurchaseListView(ListView):
    "Transaction list view"

    model = Transaction
    template_name = 'transaction/purchase_list.html'
    context_object_name = 'transaction_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['transaction_number'] = Transaction.objects.all().count()
        return context

    def get_queryset(self):
        """Returns Donation that were created today"""

        return Transaction.objects.filter(transaction_type='Purchase')


class TransactionListPurchaseFilteredView(ListView):
    "Transaction list filterd by title, location"

    model = Transaction
    template_name = 'transaction/purchase_list.html'
    context_object_name = 'filtered_transaction_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Transaction.objects.filter(
            Q(user__icontains=query) |
            Q(transaction_type__icontains='Purchase')
        )
        return object_list


class TransactionDetailView(DetailView):
    "Transaction detail view"

    model = Transaction
    template_name = 'transaction/detail.html'
    context_object_name = 'transaction'


class TransactionUpdateView(UpdateView):
    "Transaction update view"

    model = Transaction
    template_name = 'transaction/update.html'
    context_object_name = 'transaction'
    form_class = TransactionDonationCreateUpdateForm


class TransactionDeleteView(DeleteView):
    "Transaction Delete View"

    model = Transaction
    template_name = 'transaction/delete.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('transaction:transaction-list')


class TransactionCreateView(CreateView):
    "Transaction create view"

    model = Transaction
    template_name = 'transaction/create.html'
    form_class = TransactionDonationCreateUpdateForm

    def form_valid(self, form):
        user = self.request.user
        transfert_type = 'Donation'
        form.instance.user = user
        form.instance.tranfert_type = transfert_type
        return super(TransactionCreateView, self).form_valid(form)


""" class ProductTransactionTransfertCreateView(CreateView):
    "Product Transaction Transfert create view"

    model = ProductTransactionTransfert
    template_name = 'transaction/product_transaction_transfert/create.html'
    form_class = ProductTransactionTransferCreateUpdateForm """
