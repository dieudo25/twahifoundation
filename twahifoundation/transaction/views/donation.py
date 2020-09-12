from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from transaction.models.transaction import Transaction
from transaction.forms.donation import TransactionDonationCreateUpdateForm


class TransactionDonationListView(ListView):
    "Transaction list view"

    model = Transaction
    template_name = 'transaction/donation/list.html'
    context_object_name = 'transaction_list'

    def get_queryset(self):
        """Returns Donation that were created today"""

        return Transaction.objects.filter(transaction_type='Donation').exclude(with_paypal=True)


class TransactionListDonationFilteredView(ListView):
    "Transaction list filterd by title, location"

    model = Transaction
    template_name = 'transaction/donation/list.html'
    context_object_name = 'filtered_transaction_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Transaction.objects.filter(
            Q(user__username__icontains=query) |
            Q(transaction_type__icontains='Donation')
        ).exclude(with_paypal=True)
        return object_list


class TransactionDonationDetailView(DetailView):
    "Transaction detail view"

    model = Transaction
    template_name = 'transaction/donation/detail.html'
    context_object_name = 'transaction'


class TransactionDonationUpdateView(UpdateView):
    "Transaction update view"

    model = Transaction
    template_name = 'transaction/donation/update.html'
    context_object_name = 'transaction'
    form_class = TransactionDonationCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:donation-detail", kwargs={"pk": self.object.pk})


class TransactionDonationDeleteView(DeleteView):
    "Transaction Delete View"

    model = Transaction
    template_name = 'transaction/donation/delete.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('transaction:donation-list')


class TransactionDonationCreateView(CreateView):
    "Transaction create view"

    model = Transaction
    template_name = 'transaction/donation/create.html'
    form_class = TransactionDonationCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:donation-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, TransactionDonationCreateUpdateForm):
        user = self.request.user
        transfert_type = 'Donation'
        TransactionDonationCreateUpdateForm.instance.user = user
        TransactionDonationCreateUpdateForm.instance.tranfert_type = transfert_type
        return super(TransactionDonationCreateView, self).form_valid(TransactionDonationCreateUpdateForm)


def donation_validate(request, pk):

    transaction = Transaction.objects.get(pk=pk)
    transaction.validate()
    return redirect(reverse_lazy("transaction:donation-detail", kwargs={"pk": pk}))
