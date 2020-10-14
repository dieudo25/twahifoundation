from django import forms

from contact.models.person import Person
from transaction.models.transaction import Transaction


class TransactionSaleCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of a sale"

    class Meta:
        "Meta definiton for TransactionSaleCreateUpdateForm"

        model = Transaction
        fields = [
            'project',
        ]
