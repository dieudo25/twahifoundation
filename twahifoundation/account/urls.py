from django.urls import re_path
from django.contrib.auth import views as auth_views

from account.views.user import (
    UserCreateView,
    UserDetailView,
    UserDeleteView,
    UserListView,
    UserListFilteredView,
    UserUpdateView,
)

app_name = 'account'

urlpatterns = [

    # Authentication
    re_path(r'^login/$', auth_views.LoginView.as_view(
        template_name="account/auth/login.html"), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),


    # User CRUD
    re_path(r'^user/list/$', UserListView.as_view(), name="user-list"),
    re_path(r'^user/list/search/$', UserListFilteredView.as_view(),
            name="user-list-search"),
    re_path(r'^user/create/$', UserCreateView.as_view(), name="user-create"),
    re_path(r'^user/(?P<slug>[a-z0-9-]*)/$',
            UserDetailView.as_view(), name="user-detail"),
    re_path(r'^user/(?P<slug>[a-z0-9-]*)/update/$',
            UserUpdateView.as_view(), name='user-update'),
    re_path(r'^user/(?P<slug>[a-z0-9-]*)/delete/$',
            UserDeleteView.as_view(), name="user-delete"),

]
