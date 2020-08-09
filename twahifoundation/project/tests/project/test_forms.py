from django.test import TestCase

from project.models.project import Project
from project.forms.project import ProjectCreateUpdateForm


class TestForms(TestCase):
    "Test Event forms"

    def test_event_create_update_form_valid_data(self):
        "Test thee validation of the the data upon creation or update of the project"

        form = ProjectCreateUpdateForm(data={
            'title': "Project 1",
            'image': "https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            'description': "description of the project",
            'date_ended': '2016-10-25',
        })

        self.assertTrue(form.is_valid())

    def test_event_create_update_form_no_valid(self):
        ""

        form = ProjectCreateUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
