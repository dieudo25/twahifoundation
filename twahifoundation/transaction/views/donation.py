from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from notifications.models import Notification

from account.permissions.group import group_required, GroupRequiredMixin
from transaction.models.transaction import Transaction
from transaction.forms.donation import TransactionDonationCreateUpdateForm


class TransactionDonationListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Transaction list view"

    model = Transaction
    group_required = [u'Administrator', u'Member']
    template_name = 'transaction/donation/list.html'
    context_object_name = 'donation_list'
    paginate_by = 10

    def get_queryset(self):
        """Returns Donation that were created today"""

        return Transaction.objects.filter(transaction_type='Donation').exclude(with_paypal=True)


class TransactionDonationListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Transaction list filterd by title, location"

    model = Transaction
    group_required = [u'Administrator', u'Member']
    template_name = 'transaction/donation/list.html'
    context_object_name = 'filtered_donation_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Transaction.objects.filter(
            Q(user__username__icontains=query) |
            Q(transaction_type__icontains='Donation')
        ).exclude(with_paypal=True)
        return object_list


class TransactionDonationDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Transaction detail view"

    model = Transaction
    group_required = [u'Administrator', u'Member']
    template_name = 'transaction/donation/detail.html'
    context_object_name = 'transaction'

    def get_object(self):
        instance = super().get_object()

        try:
            notice_id = self.kwargs['notice_pk']
            notice = Notification.objects.get(id=notice_id)

            if notice.unread:
                notice.mark_as_read()

            return instance
        except:
            return instance


class TransactionDonationUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Transaction update view"

    model = Transaction
    group_required = [u'Administrator', u'Member']
    template_name = 'transaction/donation/update.html'
    context_object_name = 'transaction'
    form_class = TransactionDonationCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("transaction:donation-detail", kwargs={"pk": self.object.pk})


class TransactionDonationDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Transaction Delete View"

    model = Transaction
    group_required = [u'Administrator', u'Member']
    template_name = 'transaction/donation/delete.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('transaction:donation-list')


class TransactionDonationCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Transaction create view"

    model = Transaction
    group_required = [u'Administrator', u'Member']
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


class TransactionPaypalDonationList(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Transaction Paypal list view"
    model = Transaction
    group_required = [u'Administrator', u'Member']
    template_name = 'transaction/donation/paypal_list.html'
    context_object_name = 'donation_list'
    paginate_by = 10

    def get_queryset(self):
        """Returns Donation that were created today"""

        return Transaction.objects.filter(transaction_type='Donation', is_valid=True).exclude(with_paypal=False)


class TransactionPaypalDonationListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Transaction Paypallist filterd by title, location"

    model = Transaction
    group_required = [u'Administrator', u'Member']
    template_name = 'transaction/donation/paypal_list.html'
    context_object_name = 'filtered_donation_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Transaction.objects.filter(
            Q(user__username__icontains=query) |
            Q(transaction_type__icontains='Donation') |
            Q(is_valid=True)
        ).exclude(with_paypal=False)
        return object_list


@group_required('Administrateur', 'Member')
def donation_validate(request, pk):

    transaction = Transaction.objects.get(pk=pk)
    transaction.validate()
    return redirect(reverse_lazy("transaction:donation-detail", kwargs={"pk": pk}))
