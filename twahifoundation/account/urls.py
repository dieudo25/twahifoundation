from django.urls import path, include
from django.contrib.auth import views as auth_views

from account.views.user import ProfileView, ProfileUpdateView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="account/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="account/logout.html"), name='logout'),
    path('profile/<slug>/', ProfileView.as_view(), name="profile"),
    path('profile/<slug>/update/',
         ProfileUpdateView.as_view(), name='profile-update'),
]
