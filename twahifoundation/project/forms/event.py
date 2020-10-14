import pytz

from datetime import datetime
from django import forms
from django.contrib.auth import get_user
from django.utils.translation import ugettext_lazy as _

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
            'title_fr',
            'title_en',
            'project',
            'location',
            'location_fr',
            'location_en',
            'time_started',
            'time_ended',
            'event_type',
            'image',
            'content',
            'content_fr',
            'content_en',
        ]
        """ labels = {
            'title': _('Title [en]'),
            'location': _('Location [en]'),
            'content': _('Content [en]'),
        } """
        widgets = {
            'time_started': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
            'time_ended': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
        }

    def clean(self):
        cleaned_data = super(EventCreateUpdateForm, self).clean()
        time_started = cleaned_data.get("time_started")
        time_ended = cleaned_data.get("time_ended")
        now = datetime.now(pytz.timezone('Europe/Brussels'))

        if time_started and time_ended:
            if time_started < now:
                raise forms.ValidationError(
                    _("The beginning of an event cannot be in the past !"))

            elif time_ended < time_started:
                raise forms.ValidationError(
                    _("The end time of a event cannot be earlier than its start time !"))

        return cleaned_data

class EventUpdateFormLN(forms.ModelForm):
    "Customized form for the update of an event"

    class Meta:
        "Meta definiton for EventUpdateForm"

        model = Event
        fields = [
            'title_fr',
            'title_en',
            'project',
            'location_fr',
            'location_en',
            'time_started',
            'time_ended',
            'event_type',
            'image',
            'content_fr',
            'content_en',
        ]
        """ labels = {
            'title': _('Title [en]'),
            'location': _('Location [en]'),
            'content': _('Content [en]'),
        } """
        widgets = {
            'time_started': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
            'time_ended': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
        }

    def clean(self):
        cleaned_data = super(EventUpdateFormLN, self).clean()
        time_started = cleaned_data.get("time_started")
        time_ended = cleaned_data.get("time_ended")
        now = datetime.now(pytz.timezone('Europe/Brussels'))

        if time_started and time_ended:
            if time_started < now:
                raise forms.ValidationError(
                    _("The beginning of an event cannot be in the past !"))

            elif time_ended < time_started:
                raise forms.ValidationError(
                    _("The end time of a event cannot be earlier than its start time !"))

        return cleaned_data


class EventCreateFormFR(forms.ModelForm):
    "Customized form for the update of an event"

    class Meta:
        "Meta definiton for EventUpdateForm"

        model = Event
        fields = [
            'title',
            'title_en',
            'project',
            'location',
            'location_en',
            'time_started',
            'time_ended',
            'event_type',
            'image',
            'content',
            'content_en',
        ]
        """ labels = {
            'title': _('Title [en]'),
            'location': _('Location [en]'),
            'content': _('Content [en]'),
        } """
        widgets = {
            'time_started': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
            'time_ended': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
        }

    def clean(self):
        cleaned_data = super(EventCreateFormFR, self).clean()
        time_started = cleaned_data.get("time_started")
        time_ended = cleaned_data.get("time_ended")
        now = datetime.now(pytz.timezone('Europe/Brussels'))

        if time_started and time_ended:
            if time_started < now:
                raise forms.ValidationError(
                    _("The beginning of an event cannot be in the past !"))

            elif time_ended < time_started:
                raise forms.ValidationError(
                    _("The end time of a event cannot be earlier than its start time !"))

        return cleaned_data

class EventCreateFormEN(forms.ModelForm):
    "Customized form for the update of an event"

    class Meta:
        "Meta definiton for EventUpdateForm"

        model = Event
        fields = [
            'title',
            'title_fr',
            'project',
            'location',
            'location_fr',
            'time_started',
            'time_ended',
            'event_type',
            'image',
            'content',
            'content_fr',
        ]
        """ labels = {
            'title': _('Title [en]'),
            'location': _('Location [en]'),
            'content': _('Content [en]'),
        } """
        widgets = {
            'time_started': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
            'time_ended': DateTimePickerInput(format='%d/%m/%Y %H:%M'),
        }

    def clean(self):
        cleaned_data = super(EventCreateFormEN, self).clean()
        time_started = cleaned_data.get("time_started")
        time_ended = cleaned_data.get("time_ended")
        now = datetime.now(pytz.timezone('Europe/Brussels'))

        if time_started and time_ended:
            if time_started < now:
                raise forms.ValidationError(
                    _("The beginning of an event cannot be in the past !"))

            elif time_ended < time_started:
                raise forms.ValidationError(
                    _("The end time of a event cannot be earlier than its start time !"))

        return cleaned_data
