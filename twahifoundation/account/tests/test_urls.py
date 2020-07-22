from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views

from account.views.user import UserListView, UserDetailView, UserUpdateView


class TestUrls(SimpleTestCase):
    "Test account app urls"

    def test_user_list_url_resolves(self):
        "Test URL UserListView"

        url = reverse('account:user-list')
        self.assertEquals(resolve(url).func.__name__,
                          UserListView.as_view().__name__)

    def test_user_detail_url_resolves(self):
        "Test URL UserDetailView"

        url = reverse('account:user-detail', args=['user1'])
        self.assertEquals(resolve(url).func.__name__,
                          UserDetailView.as_view().__name__)

    def test_user_update_url_resolves(self):
        "Test URL UserUpdateView"

        url = reverse('account:user-update', args=['user1'])
        self.assertEquals(resolve(url).func.__name__,
                          UserUpdateView.as_view().__name__)

    def test_login_url_resolves(self):
        "Test URL auth_views - LoginView"

        url = reverse('account:login')
        self.assertEquals(resolve(url).func.__name__,
                          auth_views.LoginView.as_view().__name__)

    def test_logout_url_resolves(self):
        "Test URL auth_views - LogoutView"

        url = reverse('account:logout')
        self.assertEquals(resolve(url).func.__name__,
                          auth_views.LogoutView.as_view().__name__)
