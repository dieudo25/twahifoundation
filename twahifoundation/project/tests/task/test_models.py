import pytz

from django.test import TestCase
from django.utils import dates

from project.models.project import Project
from project.models.task import Task


class TestModels(TestCase):
    "Test Event Models"

    def setUp(self):
        "Set up Environnement for the test"

        self.project1 = Project.objects.create(
            title="Project 1",
            image="https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            description="description of the project",
        )

        self.task1 = Task.objects.create(
            title="Task 1",
            description="description of the task",
            deadline='2020-08-15',
            project=self.project1,
            state='TODO',
        )

    def test_task_is_assigned_slug_on_creation(self):
        "Test if the slug is automatically genereted upon the object creation"

        self.assertEqual(self.task1.slug, 'task-1')
