from django import forms

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
