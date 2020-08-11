from django import forms

from stock.models.category import Category


class CategoryCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for CategoryUpdateForm"

        model = Category
        fields = [
            'name',
        ]
