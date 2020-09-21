from django.urls import re_path

from portal.views.views import (
    Home,
    NotificationList,
    mark_as_read,
    mark_all_as_read,
)

app_name = 'portal'

urlpatterns = [
    re_path(r'notifications/read/all/$',
            mark_all_as_read, name="notice-read-all"),
    re_path(r'notifications/(?P<pk>\d+)/read',
            mark_as_read, name="notice-read"),
    re_path(r'^notifications/$', NotificationList.as_view(),
            name="user-notifications"),
    re_path(r'^$', Home.as_view(), name="portal-home"),


]
