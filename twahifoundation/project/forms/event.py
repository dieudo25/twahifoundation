from django import forms

from account.models.user import User
from project.models.event import Event, Project


class EventUpdateForm(forms.ModelForm):
    "Customized form for the update of an event"

    class Meta:
        "Meta definiton for EventUpdateForm"

        model = Event
        fields = [
            'title',
            'project',
            'users',
            'location',
            'time_started',
            'time_ended',
            'event_type',
            'image',
            'description',
        ]
