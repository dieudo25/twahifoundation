from django import forms

from stock.models.product import Product
from transaction.models.transaction import ProductTransactionLine


class ProductSaleTransactionLineCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of a transaction line"

    class Meta:
        "Meta definiton for ProductTransactionLineCreateUpdateForm"

        model = ProductTransactionLine
        fields = [
            'product',
            'quantity',
        ]

    def __init__(self, user=None, **kwargs):
        super(ProductSaleTransactionLineCreateUpdateForm, self).__init__(**kwargs)
        self.fields['product'].queryset = Product.objects.filter(is_saleable=True)


class ProductPurchaseTransactionLineCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of a transaction line"

    class Meta:
        "Meta definiton for ProductTransactionLineCreateUpdateForm"

        model = ProductTransactionLine
        fields = [
            'product',
            'quantity',
        ]

    def __init__(self, user=None, **kwargs):
        super(ProductPurchaseTransactionLineCreateUpdateForm, self).__init__(**kwargs)
        self.fields['product'].queryset = Product.objects.filter(is_purchasable=True)
