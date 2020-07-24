from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views

from page.views import HomeView


class TestUrls(SimpleTestCase):
    "Test page app urls"

    def test_home_resolves(self):
        "Test URL UserDetailView"

        url = reverse('page:home')
        self.assertEqual(resolve(url).func.__name__,
                         HomeView.as_view().__name__)
