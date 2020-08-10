from django.test import SimpleTestCase
from django.urls import reverse, resolve

from project.views.task import (
    TaskCreateView,
    TaskDeleteView,
    TaskListView,
    TaskListFilteredView,
    TaskDetailView,
    TaskUpdateView,
)


class TestUrls(SimpleTestCase):
    "Test task app urls"

    # CRUD

    def test_task_list_url_resolves(self):
        "Test URL TaskListView"

        url = reverse('project:task-list')
        self.assertEqual(resolve(url).func.__name__,
                         TaskListView.as_view().__name__)

    def test_task_list_filtered_url_resolves(self):
        "Test URL TaskListFilteredView"

        url = reverse('project:task-list-search')
        self.assertEqual(resolve(url).func.__name__,
                         TaskListFilteredView.as_view().__name__)

    def test_task_detail_url_resolves(self):
        "Test URL TaskDetailView"

        url = reverse('project:task-detail', args=['task1'])
        self.assertEqual(resolve(url).func.__name__,
                         TaskDetailView.as_view().__name__)

    def test_task_update_url_resolves(self):
        "Test URL TaskUpdateView"

        url = reverse('project:task-update', args=['task1'])
        self.assertEqual(resolve(url).func.__name__,
                         TaskUpdateView.as_view().__name__)

    def test_task_create_url_resolves(self):
        "Test URL TaskCreateView"

        url = reverse('project:task-create')
        self.assertEqual(resolve(url).func.__name__,
                         TaskCreateView.as_view().__name__)

    def test_task_delete_url_resolves(self):
        "Test URL TaskDeleteView"

        url = reverse('project:task-delete', args=['task1'])
        self.assertEqual(resolve(url).func.__name__,
                         TaskDeleteView.as_view().__name__)
