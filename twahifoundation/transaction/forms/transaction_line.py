from django import forms

from transaction.models.transaction import ProductTransactionLine


class ProductTransactionLineCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of a transaction line"

    class Meta:
        "Meta definiton for ProductTransactionLineCreateUpdateForm"

        model = ProductTransactionLine
        fields = [
            'product',
            'quantity',
        ]
