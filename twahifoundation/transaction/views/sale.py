from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Sum
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from account.permissions.group import group_required, GroupRequiredMixin
from transaction.models.transaction import Transaction, ProductTransactionLine
from transaction.forms.sale import TransactionSaleCreateUpdateForm
from transaction.forms.transaction_line import ProductSaleTransactionLineCreateUpdateForm


class TransactionSaleListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Transaction list view"

    model = Transaction
    group_required = [u'Administrator', u'President', u'Member']
    template_name = 'transaction/sale/list.html'
    context_object_name = 'sale_list'
    paginate_by = 10

    def get_queryset(self):
        """Returns Donation that were created today"""

        return Transaction.objects.filter(transaction_type='Sale')


class TransactionListSaleFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Transaction list filterd by title, location"

    model = Transaction
    group_required = [u'Administrator', u'President', u'Member']
    template_name = 'transaction/sale/list.html'
    context_object_name = 'filtered_sale_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Transaction.objects.filter(
            Q(user__icontains=query) |
            Q(transaction_type__icontains='Sale')
        )
        return object_list


class TransactionSaleDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Transaction detail view"

    model = Transaction
    group_required = [u'Administrator', u'President', u'Member']
    template_name = 'transaction/sale/detail.html'
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


class TransactionSaleUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Transaction update view"

    model = Transaction
    group_required = [u'Administrator', u'President', u'Member']
    template_name = 'transaction/sale/update.html'
    context_object_name = 'transaction'
    form_class = TransactionSaleCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:sale-detail", kwargs={"pk": self.object.pk})


class TransactionSaleDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Transaction Delete View"

    model = Transaction
    group_required = [u'Administrator', u'President', u'Member']
    template_name = 'transaction/sale/delete.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('transaction:sale-list')


class TransactionSaleCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Transaction create view"

    model = Transaction
    group_required = [u'Administrator', u'President', u'Member']
    template_name = 'transaction/sale/create.html'
    form_class = TransactionSaleCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:sale-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):

        form.instance.transaction_type = 'Sale'
        form.instance.user = self.request.user
        return super(TransactionSaleCreateView, self).form_valid(form)


class ProductTransactionSaleLineCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):

    model = ProductTransactionLine
    group_required = [u'Administrator', u'President', u'Member']
    template_name = 'transaction/product_transaction_line/create.html'
    form_class = ProductSaleTransactionLineCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:sale-detail", kwargs={"pk": self.object.transaction.pk})

    def form_valid(self, form):
        transaction = Transaction.objects.get(id=self.kwargs['transaction_pk'])
        form.instance.transaction = transaction
        return super(ProductTransactionSaleLineCreateView, self).form_valid(form)


class ProductTransactionSaleLineUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Transaction update view"

    model = ProductTransactionLine
    group_required = [u'Administrator', u'President', u'Member']
    template_name = 'transaction/product_transaction_line/update.html'
    context_object_name = 'transaction_line'
    form_class = ProductSaleTransactionLineCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:sale-detail", kwargs={"pk": self.object.transaction.pk})


class ProductTransactionSaleLineDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Transaction Delete View"

    model = ProductTransactionLine
    group_required = [u'Administrator', u'President', u'Member']
    template_name = 'transaction/product_transaction_line/delete.html'
    context_object_name = 'transaction_line'

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:sale-detail", kwargs={"pk": self.object.transaction.pk})


@group_required('Administrator', 'Member')
def sale_validate(request, pk):

    transaction = Transaction.objects.get(pk=pk)
    transaction.validate()
    return redirect(reverse_lazy("transaction:sale-detail", kwargs={"pk": pk}))
