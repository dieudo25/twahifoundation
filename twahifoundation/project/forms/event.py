from django import forms
from django.contrib.auth import get_user

from bootstrap_datepicker_plus import DateTimePickerInput

from account.models.user import User
from project.models.event import Event, Project


class EventCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an event"

    class Meta:
        "Meta definiton for EventUpdateForm"

        model = Event
        fields = [
            'title',
            'project',
            'location',
            'time_started',
            'time_ended',
            'event_type',
            'image',
            'description',
        ]
        help_texts = {

        }
        widgets = {
            'time_started': DateTimePickerInput(),
            'time_ended': DateTimePickerInput(),
        }
