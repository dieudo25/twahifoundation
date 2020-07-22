from django.test import TestCase

from account.models.user import User


class TestModels(TestCase):
    "Test User Models"

    def setUp(self):
        "Set up Environnement for the test"

        self.user1 = User.objects.create(username="user1")

    def test_user_is_assigned_slug_on_creation(self):
        "Test if the slug is automatically genereted upon the"

        self.assertEquals(self.user1.slug, 'user1')
