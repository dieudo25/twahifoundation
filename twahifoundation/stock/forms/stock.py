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


class ProductStockDeliveryTransferCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for StockUpdateForm"

        model = ProductStockTransfert
        fields = [
            'product',
            'quantity',
        ]

    def clean(self):
        cleaned_data = super(
            ProductStockDeliveryTransferCreateUpdateForm, self).clean()
        product = cleaned_data.get("product")
        delivery_quantity = cleaned_data.get("quantity")

        if delivery_quantity > product.quantity:
            raise forms.ValidationError(
                f"The quantity of products is too high, you currently own { product.quantity } units of { product.name }")

        return cleaned_data


class ProductStockReceptionTransferCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for StockUpdateForm"

        model = ProductStockTransfert
        fields = [
            'product',
            'quantity',
        ]
