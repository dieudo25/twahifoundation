from django.views.generic import TemplateView

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import (
    PayPalEncryptedPaymentsForm,
    PayPalPaymentsForm
)

from contact.models.person import Person
from project.models.project import Project
