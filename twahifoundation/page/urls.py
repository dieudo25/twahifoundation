from django.urls import path, include

from page.views import Home


urlpatterns = [
    path('', Home.as_view(), name="home"),
]
