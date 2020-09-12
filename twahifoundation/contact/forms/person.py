from django import forms

from contact.models.person import Person


class DonatorForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
