from django import forms

from transaction.models.transaction import Transaction


class TransactionDonationCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for StockUpdateForm"

        model = Transaction
        fields = [
            'project',
            'person',
            'total',
        ]
        labels = {
            'total': 'Amount'
        }


""" class ProductStockTransferCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for StockUpdateForm"

        model = ProductStockTransfert
        fields = [
            'transfert_type',
            'product',
            'quantity',
        ] """
