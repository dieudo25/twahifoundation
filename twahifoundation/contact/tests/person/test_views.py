import json

from django.test import TestCase, Client
from django.urls import reverse

from contact.models.person import Person


class TestViews(TestCase):
    "Test Person Views"

    def setUp(self):
        "Set up Environnement for the test"

        self.client = Client()

        self.list_url = reverse('contact:person-list')
        self.list_filtered_url = reverse('contact:person-list-search')
        self.detail_url = reverse(
            'contact:person-detail', args=['mark-avendick'])
        self.update_url = reverse(
            'contact:person-update', args=['mark-avendick'])
        self.create_url = reverse('contact:person-create')
        self.delete_url = reverse(
            'contact:person-delete', args=['mark-avendick'])

        self.person1 = Person.objects.create(
            first_name='Mark',
            last_name='Avendick',
            email="avendicM@gmail.com",
            phone_number="0476543298",
            """ is_supplier=True,
            is_donor=False,
            is_subscribed=True """
        )

    def test_person_list(self):
        "Test VIEW PersonListView"

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/person/list.html')

    def test_person_list_filtered(self):
        "Test VIEW PersonListView FILTERED"

        response = self.client.get(self.list_filtered_url, {
            'search': 'Mark'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/person/list.html')

    def test_person_detail(self):
        "Test VIEW PersonDetailView"

        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/person/detail.html')

    def test_person_updtae(self):
        "Test VIEW PersonUpdateView"

        response = self.client.post(self.update_url, {
            'first_name': 'Franck',
            'last_name': 'Pulis',
            'email': 'fkpoDon@gmail.com',
            'phone_number': '9677687698',
            """ 'is_supplier': True,
            'is_subscribed': True,
            'is_donor': True, """
        })

        updated_person = Person.objects.filter(first_name="Franck")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_person.count(), 1)

    def test_person_create(self):
        "Test VIEW PersonCreateView"

        response = self.client.post(self.create_url, {
            'first_name': 'Franckie',
            'last_name': 'Pulissa',
            'email': 'fontel@gmail.com',
            'phone_number': '97754556',
            """ 'is_supplier': False,
            'is_subscribed': False,
            'is_donor': True, """
        })

        person2 = Person.objects.get(first_name="Franckie")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(person2.first_name, 'Franckie')

    def test_person_create_no_data(self):
        "Test VIEW PersonCreateView WITHOUT data"

        response = self.client.post(self.create_url)

        person3 = Person.objects.filter(first_name="Franckie").count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(person3, 0)
        self.assertTemplateUsed(response, 'contact/person/create.html')

    def test_person_delete(self):
        "Test VIEW PersonDeleteView"

        response = self.client.delete(self.delete_url, json.dumps({
            'id': 1
        }))

        persons_number = Person.objects.all().count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(persons_number, 0)
