from django.test import SimpleTestCase
from django.urls import reverse, resolve

from project.views.project import (
    ProjectCreateView,
    ProjectDeleteView,
    ProjectListView,
    ProjectListFilteredView,
    ProjectDetailView,
    ProjectUpdateView,
)


class TestUrls(SimpleTestCase):
    "Test project app urls"

    # CRUD

    def test_project_list_url_resolves(self):
        "Test URL ProjectListView"

        url = reverse('project:project-list')
        self.assertEqual(resolve(url).func.__name__,
                         ProjectListView.as_view().__name__)

    def test_project_list_filtered_url_resolves(self):
        "Test URL ProjectListFilteredView"

        url = reverse('project:project-list-search')
        self.assertEqual(resolve(url).func.__name__,
                         ProjectListFilteredView.as_view().__name__)

    def test_project_detail_url_resolves(self):
        "Test URL ProjectDetailView"

        url = reverse('project:project-detail', args=['project1'])
        self.assertEqual(resolve(url).func.__name__,
                         ProjectDetailView.as_view().__name__)

    def test_project_update_url_resolves(self):
        "Test URL ProjectUpdateView"

        url = reverse('project:project-update', args=['project1'])
        self.assertEqual(resolve(url).func.__name__,
                         ProjectUpdateView.as_view().__name__)

    def test_project_create_url_resolves(self):
        "Test URL ProjectCreateView"

        url = reverse('project:project-create')
        self.assertEqual(resolve(url).func.__name__,
                         ProjectCreateView.as_view().__name__)

    def test_project_delete_url_resolves(self):
        "Test URL ProjectDeleteView"

        url = reverse('project:project-delete', args=['project1'])
        self.assertEqual(resolve(url).func.__name__,
                         ProjectDeleteView.as_view().__name__)
