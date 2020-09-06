from django import forms

from contact.models.person import Person
from transaction.models.transaction import Transaction


class TransactionDonationCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of a donation"

    class Meta:
        "Meta definiton for TransactionDonationCreateUpdateForm"

        model = Transaction
        fields = [
            'project',
            'person',
            'total',
        ]
        labels = {
            'total': 'Amount'
        }

    def __init__(self, user=None, **kwargs):
        super(TransactionDonationCreateUpdateForm, self).__init__(**kwargs)
        self.fields['person'].queryset = Person.objects.filter(
            is_donor=True)
