from django import forms

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
            'deadline': 'Exemple : 2006-10-25',
        }
        widgets = {
            'users': forms.CheckboxSelectMultiple,
        }
