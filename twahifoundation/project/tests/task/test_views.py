import json
import pytz

from django.urls import reverse
from django.test import Client, TestCase
from django.utils import timezone

from project.models.project import Project
from project.models.task import Task


class TestViews(TestCase):
    "Test Task Views"

    def setUp(self):
        "Set up Environnement for the test"

        self.client = Client()

        self.list_url = reverse('project:task-list')
        self.list_filtered_url = reverse('project:task-list-search')
        self.detail_url = reverse(
            'project:task-detail', args=['task-1'])
        self.update_url = reverse(
            'project:task-update', args=['task-1'])
        self.create_url = reverse('project:task-create')
        self.delete_url = reverse(
            'project:task-delete', args=['task-1'])

        self.project1 = Project.objects.create(
            title="Project 1",
            image="https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            description="description of the project",
        )

        self.task1 = Task.objects.create(
            title="Task 1",
            description="description of the task",
            deadline='2020-08-15',
            project=self.project1,
            state='TODO',
        )

        self.STATE_CHOICES = [
            ('TODO', 'TO DO'),
            ('PENDING', 'PENDING'),
            ('IN PROGRESS', 'IN PROGRESS'),
            ('LATE', 'LATE'),
            ('DONE', 'DONE')
        ]

    def test_task_list(self):
        "Test VIEW TaskListView"

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/task/list.html')

    def test_task_list_filtered(self):
        "Test VIEW TaskListView FILTERED"

        response = self.client.get(self.list_filtered_url, {
            'search': 'Task 1'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/task/list.html')

    def test_task_detail(self):
        "Test VIEW TaskDetailView"

        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/task/detail.html')

    def test_task_update(self):
        "Test VIEW TaskUpdateView"

        response = self.client.post(self.update_url, {
            'title': "Task 1",
            'project': self.project1,
            'description': "description of the task",
            'state': self.STATE_CHOICES[2][0],
            'deadline': '2026-10-25',
        })

        updated_task = Task.objects.filter(title="Task 2")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_task.count(), 1)

    def test_task_create(self):
        "Test VIEW TaskCreateView"

        response = self.client.post(self.create_url, {
            'title': "Task 2",
            'project': self.project1,
            'description': "description of the task",
            'state': self.STATE_CHOICES[0][0],
            'deadline': '2020-12-15',
        })

        task2 = Task.objects.get(title="Task 2")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(task2.title, 'Task 2')

    def test_task_create_no_data(self):
        "Test VIEW TaskCreateView WITHOUT data"

        response = self.client.post(self.create_url)

        task3 = Task.objects.filter(slug="task-2").count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(task3, 0)
        self.assertTemplateUsed(response, 'project/task/create.html')

    def test_task_delete(self):
        "Test VIEW TaskDeleteView"

        response = self.client.delete(self.delete_url, json.dumps({
            'id': 1,
        }))

        tasks_number = Task.objects.all().count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(tasks_number, 0)
