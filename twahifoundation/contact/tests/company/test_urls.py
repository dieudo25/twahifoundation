from django.test import SimpleTestCase
from django.urls import reverse, resolve

from contact.views.person import (
    PersonCreateView,
    PersonDeleteView,
    PersonListView,
    PersonListFilteredView,
    PersonDetailView,
    PersonUpdateView,
)


class TestUrls(SimpleTestCase):
    "Test contact app urls"

    # CRUD

    def test_person_list_url_resolves(self):
        "Test URL PersonListView"

        url = reverse('contact:person-list')
        self.assertEqual(resolve(url).func.__name__,
                         PersonListView.as_view().__name__)

    def test_person_list_filtered_url_resolves(self):
        "Test URL PersonListFilteredView"

        url = reverse('contact:person-list-search')
        self.assertEqual(resolve(url).func.__name__,
                         PersonListFilteredView.as_view().__name__)

    def test_person_detail_url_resolves(self):
        "Test URL PersonDetailView"

        url = reverse('contact:person-detail', args=['person1'])
        self.assertEqual(resolve(url).func.__name__,
                         PersonDetailView.as_view().__name__)

    def test_person_update_url_resolves(self):
        "Test URL PersonUpdateView"

        url = reverse('contact:person-update', args=['person1'])
        self.assertEqual(resolve(url).func.__name__,
                         PersonUpdateView.as_view().__name__)

    def test_person_create_url_resolves(self):
        "Test URL PersonCreateView"

        url = reverse('contact:person-create')
        self.assertEqual(resolve(url).func.__name__,
                         PersonCreateView.as_view().__name__)

    def test_person_delete_url_resolves(self):
        "Test URL PersonDeleteView"

        url = reverse('contact:person-delete', args=['person1'])
        self.assertEqual(resolve(url).func.__name__,
                         PersonDeleteView.as_view().__name__)
