""" import json

from django.test import TestCase, Client
from django.urls import reverse

from account.models.user import User
from account.views.user import UserDetailView


class TestViews(TestCase):
    "Test User Views"

    def setUp(self):
        "Set up Environnement for the test"

        self.client = Client()

        self.list_url = 'user/list/'
        self.detail_url = 'profile/user1/'

        self.user1 = User.objects.create_user(
            username='user1',
            password='password1'
        )

    def test_user_list_GET(self):
        "Test LIST UserListView"

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/user/list.html') """


def test_user_detail_GET(self):
    "Test VIEW UserDetailView"

    response = self.client.get(self.detail_url)

    print(response.status_code)

    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'account/user/detail.html')
