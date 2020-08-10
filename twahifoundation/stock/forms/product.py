from django import forms

from stock.models.product import Product


class ProductCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for ProductUpdateForm"

        model = Product
        fields = [
            'name',
            'category',
            'price',
            'image',
            'description',
            'is_saleable',
            'is_purchasable',
        ]
