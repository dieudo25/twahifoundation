import json

from django.test import TestCase, Client
from django.urls import reverse

from page.views import HomeView


class TestViews(TestCase):
    "Test Page Views"

    def setUp(self):
        "Set up Environnement for the test"

        self.client = Client()
        self.home_url = reverse('page:home')

    def test_user_detail_GET(self):
        "Test VIEW HomeView"

        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'page/home.html')
