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
            'content',
        ]
        help_texts = {

        }
        widgets = {
            'time_started': DateTimePickerInput(),
            'time_ended': DateTimePickerInput(),
        }

    def clean(self):
        cleaned_data = super(EventCreateUpdateForm, self).clean()
        time_started = cleaned_data.get("time_started")
        time_ended = cleaned_data.get("time_ended")

        if time_started and time_ended:
            if time_ended < time_started:
                raise forms.ValidationError(
                    "The end time of a event cannot be earlier than its start time !")
        return cleaned_data
