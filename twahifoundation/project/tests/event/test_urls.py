from django.test import SimpleTestCase
from django.urls import reverse, resolve

from project.views.event import (
    # EventCreateView,
    # EventDeleteView,
    EventListView,
    EventListFilteredView,
    # EventDetailView,
    # EventUpdateView,
)


class TestUrls(SimpleTestCase):
    "Test project app urls"

    # CRUD

    def test_event_list_url_resolves(self):
        "Test URL EventListView"

        url = reverse('project:event-list')
        self.assertEqual(resolve(url).func.__name__,
                         EventListView.as_view().__name__)

    def test_event_list_filtered_url_resolves(self):
        "Test URL EventListFilteredView"

        url = reverse('project:event-list-search')
        self.assertEqual(resolve(url).func.__name__,
                         EventListFilteredView.as_view().__name__)

    """ def test_event_detail_url_resolves(self):
        "Test URL EventDetailView"

        url = reverse('project:event-detail', args=['event1'])
        self.assertEqual(resolve(url).func.__name__,
                         EventDetailView.as_view().__name__)

    def test_event_update_url_resolves(self):
        "Test URL EventUpdateView"

        url = reverse('project:event-update', args=['event1'])
        self.assertEqual(resolve(url).func.__name__,
                         EventUpdateView.as_view().__name__)

    def test_event_create_url_resolves(self):
        "Test URL EventCreateView"

        url = reverse('project:event-create')
        self.assertEqual(resolve(url).func.__name__,
                         EventCreateView.as_view().__name__)

    def test_event_delete_url_resolves(self):
        "Test URL EventDeleteView"

        url = reverse('project:event-delete', args=['event1'])
        self.assertEqual(resolve(url).func.__name__,
                         EventDeleteView.as_view().__name__) """
