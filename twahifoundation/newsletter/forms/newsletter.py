from django import forms


class AddSubsscriberForm(forms.Form):
    email = forms.EmailField(required=True)
