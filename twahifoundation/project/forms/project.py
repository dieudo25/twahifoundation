from django import forms
from django.utils.translation import ugettext_lazy as _

from project.models.project import Project


class ProjectCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for ProjectUpdateForm"

        model = Project
        fields = [
            'title',
            'title_fr',
            'title_en',
            'image',
            'description',
            'description_fr',
            'description_en',
            'content',
            'content_fr',
            'content_en',
        ]
        """ labels = {
            'title': _('Title [en]'),
            'description': _('Description [en]'),
            'content': _('Content [en]'),
        } """

class ProjectUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for ProjectUpdateForm"

        model = Project
        fields = [
            'title_fr',
            'title_en',
            'image',
            'description_fr',
            'description_en',
            'content_fr',
            'content_en',
        ]

class ProjectCreateFormFR(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for ProjectUpdateForm"

        model = Project
        fields = [
            'title',
            'title_en',
            'image',
            'description',
            'description_en',
            'content',
            'content_en',
        ]

class ProjectCreateFormEN(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for ProjectUpdateForm"

        model = Project
        fields = [
            'title',
            'title_fr',
            'image',
            'description',
            'description_fr',
            'content',
            'content_fr',
        ]
