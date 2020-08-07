import json
import pytz

from django.urls import reverse
from django.test import Client, TestCase
from django.utils import timezone

from project.models.event import Event
from project.models.project import Project


class TestViews(TestCase):
    "Test Event Views"

    def setUp(self):
        "Set up Environnement for the test"

        self.client = Client()

        self.list_url = reverse('project:event-list')
        self.list_filtered_url = reverse('project:event-list-search')
        self.detail_url = reverse(
            'project:event-detail', args=['event-1'])
        self.update_url = reverse(
            'project:event-update', args=['event-1'])
        """ self.create_url = reverse('project:event-2')
        self.delete_url = reverse(
            'project:event-delete', args=['event-1']) """

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

    def test_event_list(self):
        "Test VIEW EventListView"

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/event/list.html')

    def test_event_list_filtered(self):
        "Test VIEW EventListView FILTERED"

        response = self.client.get(self.list_filtered_url, {
            'search': 'Event 1'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/event/list.html')

    def test_event_detail(self):
        "Test VIEW EventDetailView"

        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/event/detail.html')

    def test_event_update(self):
        "Test VIEW EventUpdateView"

        response = self.client.post(self.update_url, {
            'title': "Event 2",
            'location': "Liege",
            'event_type': "MemberMeeting",
            'image': "https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            'description': "description of the event",
            'date_created': timezone.now(),
            'time_started': timezone.datetime(
                2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
            'time_ended': timezone.datetime(
                2019, 1, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
            'project': self.project1,
        })

        updated_event = Event.objects.filter(slug="event-2")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_event.count(), 1)

    """  def test_event_create(self):
        "Test VIEW EventCreateView"

        response = self.client.post(self.create_url, {
            'name': 'MediaMarkt',
            'email': 'fontel@gmail.com',
            'phone_number': '97754556',
            'address': 'Rue de la Fontaine 345 1000 Bruxelles',
            'website': 'https://www.mediamarkt.be',
            'is_partner': True,
        })

        event2 = Event.objects.get(name="MediaMarkt")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(event2.name, 'MediaMarkt')

    def test_event_create_no_data(self):
        "Test VIEW EventCreateView WITHOUT data"

        response = self.client.post(self.create_url)

        event3 = Event.objects.filter(name="Vans").count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(event3, 0)
        self.assertTemplateUsed(response, 'project/event/create.html')

    def test_event_delete(self):
        "Test VIEW EventDeleteView"

        response = self.client.delete(self.delete_url, json.dumps({
            'id': 1
        }))

        companies_number = Event.objects.all().count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(companies_number, 0)
 """
