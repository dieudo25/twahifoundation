from django import forms
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    gdpr = forms.BooleanField(required=True,
        label=_("<span>Yes, I consent to my data being stored according to the guidelines set out in the <a href='/page/legal-mentions/'>Privacy Policy</a>.</span>"))

