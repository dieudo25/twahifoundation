from django.test import TestCase

from contact.models.person import Person
from contact.models.company import Company


class TestModels(TestCase):
    "Test Person Models"

    def setUp(self):
        "Set up Environnement for the test"

        self.company1 = Company.objects.create(
            name="Tesla",
            address="adress of tesla",
            email="tesla@info.com",
            phone_number="0678987865",
            website="www.tesla.com",
            is_partner=True,
        )

    def test_user_is_assigned_slug_on_creation(self):
        "Test if the slug is automatically genereted upon the object creation"

        self.assertEqual(self.person1.slug, 'mark-avendick')
