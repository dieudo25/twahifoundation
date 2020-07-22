from django.urls import path, include

from portal.views.views import Home

app_name = 'portal'

urlpatterns = [
    path('', Home.as_view(), name="portal-home"),
]
