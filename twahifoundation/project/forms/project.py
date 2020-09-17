from django import forms

from project.models.project import Project


class ProjectCreateUpdateForm(forms.ModelForm):
    "Customized form for the update of an project"

    class Meta:
        "Meta definiton for ProjectUpdateForm"

        model = Project
        fields = [
            'title',
            'image',
            'description',
            'content',
        ]
