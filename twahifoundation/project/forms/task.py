from django import forms

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
            'deadline': DatePickerInput()
        }
