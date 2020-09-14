from django import forms

from blog.models.tags import Tags


class TagsCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for CategoryUpdateForm"

        model = Tags
        fields = [
            'name',
        ]
