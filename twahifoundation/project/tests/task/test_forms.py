""" from django.test import TestCase

from project.models.project import Project
from project.models.task import Task
from project.forms.task import TaskCreateUpdateForm


class TestForms(TestCase):
    "Test Task forms"

    def setUp(self):
        "Set up Environnement for the test"

        self.project1 = Project.objects.create(
            title="Project 1",
            image="https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            description="description of the project",
            date_created="Aug. 1, 2020",
        )

    def test_task_create_update_form_valid_data(self):
        "Test thee validation of the the data upon creation or update of the task"

        STATE_CHOICES = [
            ('TODO', 'TO DO'),
            ('PENDING', 'PENDING'),
            ('IN PROGRESS', 'IN PROGRESS'),
            ('LATE', 'LATE'),
            ('DONE', 'DONE')
        ]

        form = TaskCreateUpdateForm(data={
            'title': "Task 1",
            'project': self.project1,
            'description': "description of the task",
            'state': STATE_CHOICES[0][0],
            'deadline': '2016-10-25',
        })

        self.assertTrue(form.is_valid())

    def test_task_create_update_form_no_valid(self):
        ""

        form = TaskCreateUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

 """
