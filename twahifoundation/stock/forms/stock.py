from django import forms

from stock.models.stock import Stock, ProductStockTransfert


class StockCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for StockUpdateForm"

        model = Stock
        fields = [
            'name',
            'location',
        ]


class ProductStockTransferCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for StockUpdateForm"

        model = ProductStockTransfert
        fields = [
            'product',
            'quantity',
        ]
