from django.urls import path, include

from portal.views.views import Home


urlpatterns = [
    path('', Home.as_view(), name="portal-home"),
]
