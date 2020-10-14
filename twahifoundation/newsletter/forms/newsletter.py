from django import forms


class AddSubsscriberForm(forms.Form):
    email = forms.EmailField(required=True)


class GDPRForm(forms.Form):

    gdpr = forms.BooleanField(required=True,
        label=_("<span>Yes, I consent to my data being stored according to the guidelines set out in the <a href='/page/legal-mentions/'>Privacy Policy</a>.</span>"))
