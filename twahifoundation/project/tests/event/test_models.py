import pytz

from django.test import TestCase
from django.utils import timezone

from project.models.event import Event
from project.models.project import Project


class TestModels(TestCase):
    "Test Event Models"

    def setUp(self):
        "Set up Environnement for the test"

        self.project1 = Project.objects.create(
            title="Project 1",
            image="https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            description="description of the project",
            date_created="Aug. 1, 2020",
        )

        self.event1 = Event.objects.create(
            title="Event 1",
            location="Bruxelles",
            event_type="MemberMeeting",
            image="https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            description="description of the event",
            date_created=timezone.now(),
            time_started=timezone.datetime(
                2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
            time_ended=timezone.datetime(
                2019, 1, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
            project=self.project1,
        )

    def test_event_is_assigned_slug_on_creation(self):
        "Test if the slug is automatically genereted upon the object creation"

        self.assertEqual(self.event1.slug, 'event-1')
