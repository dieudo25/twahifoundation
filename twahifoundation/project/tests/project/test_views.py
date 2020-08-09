import json
import pytz

from django.urls import reverse
from django.test import Client, TestCase
from django.utils import timezone

from project.models.project import Project


class TestViews(TestCase):
    "Test Project Views"

    def setUp(self):
        "Set up Environnement for the test"

        self.client = Client()

        self.list_url = reverse('project:project-list')
        self.list_filtered_url = reverse('project:project-list-search')
        self.detail_url = reverse(
            'project:project-detail', args=['project-1'])
        self.update_url = reverse(
            'project:project-update', args=['project-1'])
        self.create_url = reverse('project:project-create')
        self.delete_url = reverse(
            'project:project-delete', args=['project-1'])

        self.project1 = Project.objects.create(
            title="Project 1",
            image="https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            description="description of the project",
        )

    def test_project_list(self):
        "Test VIEW ProjectListView"

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/project/list.html')

    def test_project_list_filtered(self):
        "Test VIEW ProjectListView FILTERED"

        response = self.client.get(self.list_filtered_url, {
            'search': 'Project 1'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/project/list.html')

    def test_project_detail(self):
        "Test VIEW ProjectDetailView"

        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/project/detail.html')

    def test_project_update(self):
        "Test VIEW ProjectUpdateView"

        response = self.client.post(self.update_url, {
            'title': "Project 2",
            'image': "https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            'description': "description of the project",
            'date_ended': '2016-10-25',
        })

        print(response)

        updated_project = Project.objects.filter(title="Project 2")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_project.count(), 1)

    def test_project_create(self):
        "Test VIEW ProjectCreateView"

        response = self.client.post(self.create_url, {
            'title': "Project 3",
            'image': "https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            'description': "description of the project",
            'date_ended': '2016-10-25',
        })

        project2 = Project.objects.get(title="Project 3")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(project2.title, 'Project 3')

    def test_project_create_no_data(self):
        "Test VIEW ProjectCreateView WITHOUT data"

        response = self.client.post(self.create_url)

        project3 = Project.objects.filter(slug="project-2").count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(project3, 0)
        self.assertTemplateUsed(response, 'project/project/create.html')

    def test_project_delete(self):
        "Test VIEW ProjectDeleteView"

        response = self.client.delete(self.delete_url, json.dumps({
            'id': 1
        }))

        projects_number = Project.objects.all().count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(projects_number, 0)
