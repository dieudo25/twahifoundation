from django.urls import re_path

from stock.views.product import (
    ProductListView,
    ProductListFilteredView,
    ProductDetailView,
    ProductUpdateView,
    ProductCreateView,
    ProductDeleteView,
)

app_name = 'stock'

urlpatterns = [

    # Category CRUD

    # Product CRUD
    re_path(r'^product/list/$', ProductListView.as_view(), name="product-list"),
    re_path(r'^product/list/search/$', ProductListFilteredView.as_view(),
            name="product-list-search"),
    re_path(r'^product/create/$', ProductCreateView.as_view(),
            name="product-create"),
    re_path(r'^product/(?P<slug>[a-z0-9-]*)/$',
            ProductDetailView.as_view(), name="product-detail"),
    re_path(r'^product/(?P<slug>[a-z0-9-]*)/update/$',
            ProductUpdateView.as_view(), name="product-update"),
    re_path(r'^product/(?P<slug>[a-z0-9-]*)/delete/$',
            ProductDeleteView.as_view(), name="product-delete"),

    # Stock CRUD

]
