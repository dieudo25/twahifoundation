from django.urls import re_path
from django.contrib.auth import views as auth_views

from blog.views.post import (
    PostCreateView,
    PostDetailView,
    PostDeleteView,
    PostListView,
    PostListFilteredView,
    PostUpdateView,
    PageListView,
    PageListFilteredView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
)

app_name = 'blog'

urlpatterns = [

    # Post
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

    # Static page
    re_path(r'^page/list/$', PageListView.as_view(), name="page-list"),
    re_path(r'^page/list/search/$', PageListFilteredView.as_view(),
            name="page-list-search"),
    re_path(r'^page/create/$', PageCreateView.as_view(),
            name="page-create"),
    re_path(r'^page/(?P<slug>[a-z0-9-]*)/$',
            PostDetailView.as_view(template_name="blog/page/detail.html"), name="page-detail"),
    re_path(r'^page/(?P<slug>[a-z0-9-]*)/update/$',
            PageUpdateView.as_view(), name="page-update"),

    re_path(r'^page/(?P<slug>[a-z0-9-]*)/delete/$',
            PageDeleteView.as_view(), name="page-delete"),
]
