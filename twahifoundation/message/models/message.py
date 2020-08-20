from django.db import models
from django.urls import reverse

from django_messages.models import Message


class CustomMessage(Message):
    "Custom Message class from django_messages app"

    uploaded_file = models.FileField(
        upload_to='messages/%Y/%m/%D',
        max_length=100,
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse('message:message-detail', args=[self.pk])
