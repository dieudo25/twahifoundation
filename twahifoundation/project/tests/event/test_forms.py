""" from django.test import TestCase

from project.models.project import Project
from project.forms.event import EventCreateUpdateForm


class TestForms(TestCase):
    "Test Event forms"

    def setUp(self):
        "Set up Environnement for the test"

        self.project1 = Project.objects.create(
            title="Project 1",
            image="https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            description="description of the project",
            date_created="Aug. 1, 2020",
        )

    def test_event_create_update_form_valid_data(self):
        "Test thee validation of the the data upon creation or update of the Event"

        EVENT_TYPE_CHOICES = [
            ('MemberMeeting', 'Meeting between members'),
            ('FundRaising', 'Fund rainsing'),
        ]

        form = EventCreateUpdateForm(data={
            'title': "Event 2",
            'location': "Liege",
            'event_type': EVENT_TYPE_CHOICES[0][0],
            'image': "https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            'description': "description of the event",
            'time_started': '2006-10-25 14:30',
            'time_ended': '2016-10-25 14:30',
            'project': self.project1,
        })
        print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
        print(form.errors)
        print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')

        self.assertTrue(form.is_valid())

    def test_event_create_update_form_no_valid(self):
        ""

        form = EventCreateUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)
 """
