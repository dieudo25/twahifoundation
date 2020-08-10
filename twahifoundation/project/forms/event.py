from django import forms

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
            'users',
            'location',
            'time_started',
            'time_ended',
            'event_type',
            'image',
            'description',
        ]
        help_texts = {
            'time_started': 'Exemple : 2006-10-25 14:30',
            'time_ended': 'Exemple : 2006-10-25 14:30',
        }
        widgets = {
            'users': forms.CheckboxSelectMultiple,
        }
