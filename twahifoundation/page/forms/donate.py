from paypal.standard.forms import PayPalPaymentsForm
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django import forms

from paypal.standard.conf import (
    DONATION_BUTTON_IMAGE
)

from transaction.models.transaction import Transaction
from project.models.project import Project


class DonationForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = [
            'project',
        ]

    def __init__(self, user=None, **kwargs):
        super(DonationForm, self).__init__(**kwargs)
        self.fields['project'].queryset = Project.objects.filter(
            is_deleted=False, status='Published', is_closed='False')


class PriceFieldDonationForm(forms.Form):

    AMOUNT = (
        (10.00, '10€'),
        (20.00, '20€'),
        (30.00, '30€'),
        (40.00, '40€'),
        (50.00, '50€'),
    )

    total = forms.ChoiceField(
        choices=AMOUNT, widget=forms.RadioSelect(), label='Amount')

class GDPRForm(forms.Form):

    gdpr = forms.BooleanField(required=True,
        label=_("<span>Yes, I consent to my data being stored according to the guidelines set out in the <a href='/page/legal-mentions/'>Privacy Policy</a>.</span>"))


class ExtPayPalPaymentsForm(PayPalPaymentsForm):

    def render(self):
        # format html as you need
        form_open = u'''<form class="paypal-form" action="%s" method="post">''' % (
            self.get_endpoint())
        form_close = u'</form>'
        submit_elm = u'''<input type="submit" value="DONATE"class="btn-green">'''
        return format_html(form_open+self.as_p()+submit_elm+form_close)
