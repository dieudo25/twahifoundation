from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView

from paypal.standard.forms import PayPalPaymentsForm

from page.forms.donate import DonationForm, ExtPayPalPaymentsForm, PriceFieldDonationForm
from contact.forms.person import DonatorForm
from contact.models.person import Person
from transaction.models.transaction import Transaction


class DonateView(CreateView):
    "Donate view"

    model = Transaction
    template_name = "page/static_page/donate/donate.html"
    context_object_name = 'donation'
    form_class = DonationForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy('page:donate-checkout', kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['donator_form'] = DonatorForm
        context['price_form'] = PriceFieldDonationForm
        return context

    def form_valid(self, form):
        user = self.request.user
        transaction_type = 'Donation'
        price = self.request.POST.get("total")

        form.instance.user = user
        form.instance.total = price
        form.instance.transaction_type = transaction_type
        form.instance.with_paypal = True

        first_name = self.request.POST.get("first_name")
        last_name = self.request.POST.get('last_name')
        email = self.request.POST.get('email')

        Person.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_donor=True,
        )
        person = Person.objects.get(
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_donor=True,
        )
        form.instance.person = person

        return super(DonateView, self).form_valid(form)


def donate_checkout_view(request, pk):

    transaction = get_object_or_404(Transaction, pk=pk)
    item_name = f'{ transaction } - { transaction.project }'

    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": transaction.total,
        "item_name": item_name,
        "invoice": transaction.pk,
        "currency_code": "EUR",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('page:donate-success', kwargs={'pk': transaction.pk})),
        "cancel_return": request.build_absolute_uri(reverse('page:donate-cancel', kwargs={'pk': transaction.pk})),
    }

    # Create the instance.
    form = ExtPayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "page/static_page/donate/checkout.html", context)


class DonationSuccesView(TemplateView):

    template_name = "page/static_page/donate/success.html"

    def dispatch(self, request, *args, **kwargs):
        transaction_id = self.kwargs['pk']
        transaction = get_object_or_404(Transaction, pk=transaction_id)
        transaction.validate()
        return super().dispatch(request, *args, **kwargs)


class DonationCancelView(TemplateView):

    template_name = "page/static_page/donate/cancel.html"

    def dispatch(self, request, *args, **kwargs):
        transaction_id = self.kwargs['pk']
        transaction = get_object_or_404(Transaction, pk=transaction_id)
        transaction.delete()
        return super().dispatch(request, *args, **kwargs)
