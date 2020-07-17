from django.urls import path, include
from django.contrib.auth import views as auth_views

from account.views.user import ProfileView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="account/login.html"), name='login'),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
]
