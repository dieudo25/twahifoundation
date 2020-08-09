import pytz

from django.test import TestCase
from django.utils import timezone

from project.models.project import Project


class TestModels(TestCase):
    "Test Event Models"

    def setUp(self):
        "Set up Environnement for the test"

        self.project1 = Project.objects.create(
            title="Project 1",
            image="https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            description="description of the project",
        )

    def test_event_is_assigned_slug_on_creation(self):
        "Test if the slug is automatically genereted upon the object creation"

        self.assertEqual(self.project1.slug, 'project-1')
