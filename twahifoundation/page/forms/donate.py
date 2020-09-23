from paypal.standard.forms import PayPalPaymentsForm
from django.utils.html import format_html
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
            is_deleted=False, status='Published')


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


class ExtPayPalPaymentsForm(PayPalPaymentsForm):

    def render(self):
        # format html as you need
        form_open = u'''<form class="paypal-form" action="%s" method="post">''' % (
            self.get_endpoint())
        form_close = u'</form>'
        submit_elm = u'''<input type="submit" value="DONATE"class="btn-green">'''
        return format_html(form_open+self.as_p()+submit_elm+form_close)
