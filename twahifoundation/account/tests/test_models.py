from django.test import TestCase

from contact.models.person import Person


class TestModels(TestCase):
    "Test User Models"

    def setUp(self):
        "Set up Environnement for the test"

        self.person1 = Person.objects.create(
            first_name="Alice",
            last_name="Trat",
            email="aliceTrat@gmail.com",
            phone_number="0456747567",
            is_donor=True,
            is_follower=False,
            is_supplier=True,
        )

    def test_person_is_assigned_slug_on_creation(self):
        "Test if the slug is automatically genereted upon the"

        self.assertEqual(self.person1.slug, 'alice-trat')
