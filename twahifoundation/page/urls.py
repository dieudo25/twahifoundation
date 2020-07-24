from django.urls import re_path

from page.views import HomeView

app_name = 'page'

urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name="home"),
]
