from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views

from account.views.user import (
    UserCreateView,
    UserDeleteView,
    UserListView,
    UserListFilteredView,
    UserDetailView,
    UserUpdateView,
)


class TestUrls(SimpleTestCase):
    "Test account app urls"

    # CRUD

    def test_user_list_url_resolves(self):
        "Test URL UserListView"

        url = reverse('user-list')
        self.assertEqual(resolve(url).func.__name__,
                         UserListView.as_view().__name__)

    def test_user_list_filtered_url_resolves(self):
        "Test URL UserListFilteredView"

        url = reverse('user-list-search')
        self.assertEqual(resolve(url).func.__name__,
                         UserListFilteredView.as_view().__name__)

    def test_user_detail_url_resolves(self):
        "Test URL UserDetailView"

        url = reverse('user-detail', args=['user1'])
        self.assertEqual(resolve(url).func.__name__,
                         UserDetailView.as_view().__name__)

    def test_user_update_url_resolves(self):
        "Test URL UserUpdateView"

        url = reverse('user-update', args=['user1'])
        self.assertEqual(resolve(url).func.__name__,
                         UserUpdateView.as_view().__name__)

    def test_user_create_url_resolves(self):
        "Test URL UserCreateView"

        url = reverse('user-create')
        self.assertEqual(resolve(url).func.__name__,
                         UserCreateView.as_view().__name__)

    def test_user_delete_url_resolves(self):
        "Test URL UserDeleteView"

        url = reverse('user-delete', args=['user1'])
        self.assertEqual(resolve(url).func.__name__,
                         UserDeleteView.as_view().__name__)

    # Authentification

    def test_login_url_resolves(self):
        "Test URL auth_views - LoginView"

        url = reverse('login')
        self.assertEqual(resolve(url).func.__name__,
                         auth_views.LoginView.as_view().__name__)

    def test_logout_url_resolves(self):
        "Test URL auth_views - LogoutView"

        url = reverse('logout')
        self.assertEqual(resolve(url).func.__name__,
                         auth_views.LogoutView.as_view().__name__)
