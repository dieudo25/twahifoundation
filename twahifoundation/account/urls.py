from django.urls import path, include
from django.contrib.auth import views as auth_views

from account.views.user import UserCreateView, UserDetailView, UserDeleteView, UserListView, UserUpdateView

app_name = 'account'

urlpatterns = [

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name="account/auth/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    # User
    path('user/list/', UserListView.as_view(), name="user-list"),
    path('user/<slug>/', UserDetailView.as_view(), name="user-detail"),
    path('user/<slug>/update/',
         UserUpdateView.as_view(), name='user-update'),
    path('user/<slug>/delete', UserDeleteView.as_view(), name="user-delete"),
    path('user/create', UserCreateView.as_view(), name="user-create")

]
