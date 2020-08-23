from django.views.generic import TemplateView

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import (
    PayPalEncryptedPaymentsForm,
    PayPalPaymentsForm
)

from contact.models.person import Person
from project.models.project import Project


class PaypalCheckoutView(TemplateView):
    "PaypalCheckout page"

    template_name = 'page/donate/checkout.html'


""" def donate(request, **kwargs):

    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    project = request.GET.get('project')
    amount = request.GET.get('amount')
    host = request.get_host()

    donator = Person.objects.get_or_create(
        first_name=first_name,
        last_name=last_name,
        email=email
    )

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        "amount": amount,
        "currency_code": "EUR",
        "item_name": f'Donation for the project "{project.title}" ',
        "invoice": reservation.pk,
        "notify_url": 'http://{}{}'.format(host, reverse('paypal-ipn')),
        "return_url": 'http://{}{}'.format(host, reverse('paypalreturn',
                                                         kwargs={'pk': reservation.pk})),
        "cancel_return": 'http://{}{}'.format(host, reverse('paypalcancel',
                                                            kwargs={'pk': reservation.pk})),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}

    return render(request, 'app/reservationview.html', context)
 """
