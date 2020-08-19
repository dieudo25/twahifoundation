from django.urls import re_path
from django.contrib.auth import views as auth_views

from blog.views.post import (
    PostCreateView,
    PostDetailView,
    PostDeleteView,
    PostListView,
    PostListFilteredView,
    PostUpdateView,
)

app_name = 'blog'

urlpatterns = [
    re_path(r'^post/list/$', PostListView.as_view(), name="post-list"),
    re_path(r'^post/list/search/$', PostListFilteredView.as_view(),
            name="post-list-search"),
    re_path(r'^post/create/$', PostCreateView.as_view(),
            name="post-create"),
    re_path(r'^post/(?P<slug>[a-z0-9-]*)/$',
            PostDetailView.as_view(), name="post-detail"),
    re_path(r'^post/(?P<slug>[a-z0-9-]*)/update/$',
            PostUpdateView.as_view(), name="post-update"),

    re_path(r'^post/(?P<slug>[a-z0-9-]*)/delete/$',
            PostDeleteView.as_view(), name="post-delete"),
]
