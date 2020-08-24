import json

from django.test import TestCase, Client
from django.urls import reverse

from account.models.user import User
from account.views.user import UserDetailView


class TestViews(TestCase):
    "Test User Views"

    def setUp(self):
        "Set up Environnement for the test"

        self.client = Client()

        self.list_url = reverse('user-list')
        self.list_filtered_url = reverse('user-list-search')
        self.detail_url = reverse('user-detail', args=['user1'])
        self.create_url = reverse('user-create')
        self.delete_url = reverse('user-delete', args=['user1'])

        self.user1 = User.objects.create_user(
            username='user1',
            password='password1'
        )

    def test_user_list(self):
        "Test VIEW UserListView"

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/user/list.html')

    def test_user_list_filtered(self):
        "Test VIEW UserListView FILTERED"

        response = self.client.get(self.list_filtered_url, {
            'search': 'user1'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/user/list.html')

    def test_user_detail(self):
        "Test VIEW UserDetailView"

        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/user/detail.html')

    def test_user_create(self):
        "Test VIEW UserCreateView"

        response = self.client.post(self.create_url, {
            'username': 'user2',
            'first_name': 'Anne',
            'last_name': 'Don',
            'email': 'anneDon@gmail.com',
            'password1': 'PasswordTest135',
            'password2': 'PasswordTest135'
        })

        user2 = User.objects.get(username="user2")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(user2.username, 'user2')

    def test_user_create_no_data(self):
        "Test VIEW UserCreateView WITHOUT data"

        response = self.client.post(self.create_url)

        user2 = User.objects.filter(username="user2").count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user2, 0)
        self.assertTemplateUsed(response, 'account/user/create.html')

    def test_user_delete(self):
        "Test VIEW UserDeleteView"

        response = self.client.delete(self.delete_url, json.dumps({
            'id': 1
        }))

        users_number = User.objects.all().count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(users_number, 0)


""" from django.test.utils import override_settings
import tempfile

MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestViewsWithImageField(TestCase):
    ""

    def _create_image(self):
        # create a valid image and adds it to a temporary file
        from PIL import Image

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
            image = Image.new('RGB', (200, 200), 'white')
            image.save(f, 'PNG')

        return open(f.name, mode='rb')

    def setUp(self):
        #Set up Environnement for the test"

        self.image = self._create_image()
        self.update_url = reverse('user-update', args=['user1'])

        self.user1 = User.objects.create_user(
            username='user1',
            password='password1'
        )

    def tearDown(self):
        self.image.close()

    def test_user_update(self):
        "Test VIEW UserUpdateView"

        response = self.client.post(self.update_url, {
            'username': 'user1_updated',
            'first_name': 'Franck',
            'last_name': 'Pulis',
            'email': 'fkpoDon@gmail.com',
            'avatar': self.image,
        })

        updated_user = User.objects.filter(username="user1_updated")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/user/update.html')
        self.assertEqual(updated_user.count(), 1) """
