import pytz

from datetime import date
from django import forms
from django.utils.translation import ugettext_lazy as _

from bootstrap_datepicker_plus import DatePickerInput

from account.models.user import User
from project.models.task import Task


class TaskCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an event"

    class Meta:
        "Meta definiton for EventUpdateForm"

        model = Task
        fields = [
            'title',
            'project',
            'state',
            'users',
            'description',
            'deadline'

        ]
        help_texts = {

        }

        widgets = {
            'users': forms.CheckboxSelectMultiple,
            'deadline': DatePickerInput(format='%d/%m/%Y'),
        }

    def clean(self):
        cleaned_data = super(TaskCreateUpdateForm, self).clean()
        deadline = cleaned_data.get("deadline")
        now = date.today()

        if deadline:
            if deadline < now:
                raise forms.ValidationError(
                    _("The beginning of an event cannot be in the past !"))

        return cleaned_data

class TaskUpdateForm(forms.ModelForm):
    "Customized form for the update of an event"

    class Meta:
        "Meta definiton for EventUpdateForm"

        model = Task
        fields = [
            'title_fr',
            'title_en',
            'project',
            'state',
            'users',
            'description_fr',
            'description_en',
            'deadline'

        ]
        help_texts = {

        }

        widgets = {
            'users': forms.CheckboxSelectMultiple,
            'deadline': DatePickerInput(format='%d/%m/%Y'),
        }

    def clean(self):
        cleaned_data = super(TaskUpdateForm, self).clean()
        deadline = cleaned_data.get("deadline")
        now = date.today()

        if deadline:
            if deadline < now:
                raise forms.ValidationError(
                    _("The beginning of an event cannot be in the past !"))

        return cleaned_data

class TaskCreateFormEN(forms.ModelForm):
    "Customized form for the update of an event"

    class Meta:
        "Meta definiton for EventUpdateForm"

        model = Task
        fields = [
            'title',
            'title_fr',
            'project',
            'state',
            'users',
            'description',
            'description_fr',
            'deadline'

        ]
        help_texts = {

        }

        widgets = {
            'users': forms.CheckboxSelectMultiple,
            'deadline': DatePickerInput(format='%d/%m/%Y'),
        }

    def clean(self):
        cleaned_data = super(TaskCreateFormEN, self).clean()
        deadline = cleaned_data.get("deadline")
        now = date.today()

        if deadline:
            if deadline < now:
                raise forms.ValidationError(
                    _("The beginning of an event cannot be in the past !"))

        return cleaned_data

class TaskCreateFormFR(forms.ModelForm):
    "Customized form for the update of an event"

    class Meta:
        "Meta definiton for EventUpdateForm"

        model = Task
        fields = [
            'title',
            'title_en',
            'project',
            'state',
            'users',
            'description',
            'description_en',
            'deadline'

        ]
        help_texts = {

        }

        widgets = {
            'users': forms.CheckboxSelectMultiple,
            'deadline': DatePickerInput(format='%d/%m/%Y'),
        }

    def clean(self):
        cleaned_data = super(TaskCreateFormFR, self).clean()
        deadline = cleaned_data.get("deadline")
        now = date.today()

        if deadline:
            if deadline < now:
                raise forms.ValidationError(
                    _("The beginning of an event cannot be in the past !"))

        return cleaned_data
