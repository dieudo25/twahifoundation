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

from account.views.group import (
    GroupListView,
    GroupListFilteredView,
    GroupDetailView,
)

urlpatterns = [

    # Authentication
    re_path(r'^login/$', auth_views.LoginView.as_view(
        template_name="account/auth/login.html"), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # Password Change
    re_path(r'^password/change/$',
            auth_views.PasswordChangeView.as_view(
                template_name="account/auth/password_change_form.html"
            ),
            name='password_change_form'),
    re_path(r'^password/change/done/$',
            auth_views.PasswordChangeDoneView.as_view(
                template_name="account/auth/password_change_done.html"
            ),
            name='password_change_done'),

    # Password Reset
    re_path(r'^password/reset/$',
            auth_views.PasswordResetView.as_view(
                template_name="account/auth/password_reset_form.html"
            ),
            name='password-reset'),
    re_path(r'^password/reset/done/$',
            auth_views.PasswordResetDoneView.as_view(
                template_name="account/auth/password_reset_done.html"
            ),
            name='password_reset_done'),
    re_path(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(
                template_name="account/auth/password_reset_confirm.html"),
            name='password_reset_confirm'),
    re_path(r'^reset/complete/$',
            auth_views.PasswordResetCompleteView.as_view(
                template_name="account/auth/password_reset_complete.html"
            ),
            name='password_reset_complete'),


    # Group CRUD
    re_path(r'^group/list/$', GroupListView.as_view(), name="group-list"),
    re_path(r'^group/list/search/$', GroupListFilteredView.as_view(),
            name="group-list-search"),
    re_path(r'^group/(?P<pk>[0-9-]*)/$',
            GroupDetailView.as_view(), name="group-detail"),


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
