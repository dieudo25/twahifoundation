from django import forms

from transaction.models.transaction import Transaction


class TransactionPurchaseCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of a purchase"

    class Meta:
        "Meta definiton for TransactionPurchaseCreateUpdateForm"

        model = Transaction
        fields = [
            'project',
            'person',
        ]
