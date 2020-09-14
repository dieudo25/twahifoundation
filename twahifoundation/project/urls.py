from django.urls import re_path

from project.views.event import (
    EventListView,
    EventListFilteredView,
    EventDetailView,
    EventUpdateView,
    EventCreateView,
    EventDeleteView,
    participate,
)
from project.views.project import (
    ProjectListView,
    ProjectListFilteredView,
    ProjectDetailView,
    ProjectUpdateView,
    ProjectCreateView,
    ProjectDeleteView,
)
from project.views.task import (
    TaskListView,
    TaskListFilteredView,
    TaskDetailView,
    TaskUpdateView,
    TaskCreateView,
    TaskDeleteView,
)

app_name = 'project'

urlpatterns = [

    # Event CRUD
    re_path(r'^event/list/$', EventListView.as_view(), name="event-list"),
    re_path(r'^event/list/search/$', EventListFilteredView.as_view(),
            name="event-list-search"),
    re_path(r'^event/create/$', EventCreateView.as_view(),
            name="event-create"),
    re_path(r'^post/(?P<slug>[a-z0-9-]*)/(?P<notice_pk>[0-9]*)$',
            EventDetailView.as_view(), name="event-detail-notice"),
    re_path(r'^event/(?P<slug>[a-z0-9-]*)/$',
            EventDetailView.as_view(), name="event-detail"),
    re_path(r'^event/(?P<slug>[a-z0-9-]*)/update/$',
            EventUpdateView.as_view(), name="event-update"),
    re_path(r'^event/(?P<slug>[a-z0-9-]*)/delete/$',
            EventDeleteView.as_view(), name="event-delete"),
    re_path(r'^event/(?P<slug>[a-z0-9-]*)/participate/$',
            participate, name="event-participate"),

    # Project CRUD
    re_path(r'^project/list/$', ProjectListView.as_view(), name="project-list"),
    re_path(r'^project/list/search/$', ProjectListFilteredView.as_view(),
            name="project-list-search"),
    re_path(r'^project/create/$', ProjectCreateView.as_view(),
            name="project-create"),
    re_path(r'^project/(?P<slug>[a-z0-9-]*)/(?P<notice_pk>[0-9]*)$',
            ProjectDetailView.as_view(), name="project-detail-notice"),
    re_path(r'^project/(?P<slug>[a-z0-9-]*)/$',
            ProjectDetailView.as_view(), name="project-detail"),
    re_path(r'^project/(?P<slug>[a-z0-9-]*)/update/$',
            ProjectUpdateView.as_view(), name="project-update"),
    re_path(r'^project/(?P<slug>[a-z0-9-]*)/delete/$',
            ProjectDeleteView.as_view(), name="project-delete"),

    # Task CRUD
    re_path(r'^task/list/$', TaskListView.as_view(), name="task-list"),
    re_path(r'^task/list/search/$', TaskListFilteredView.as_view(),
            name="task-list-search"),
    re_path(r'^task/create/$', TaskCreateView.as_view(),
            name="task-create"),
    re_path(r'^post/(?P<slug>[a-z0-9-]*)/(?P<notice_pk>[0-9]*)$',
            TaskDetailView.as_view(), name="task-detail-notice"),
    re_path(r'^task/(?P<slug>[a-z0-9-]*)/$',
            TaskDetailView.as_view(), name="task-detail"),
    re_path(r'^task/(?P<slug>[a-z0-9-]*)/update/$',
            TaskUpdateView.as_view(), name="task-update"),
    re_path(r'^task/(?P<slug>[a-z0-9-]*)/delete/$',
            TaskDeleteView.as_view(), name="task-delete"),



]
