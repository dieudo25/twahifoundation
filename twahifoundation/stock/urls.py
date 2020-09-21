from django.urls import re_path

from stock.views.category import (
    CategoryListView,
    CategoryListFilteredView,
    CategoryUpdateView,
    CategoryCreateView,
    CategoryDeleteView,
)
from stock.views.product import (
    ProductListView,
    ProductListFilteredView,
    ProductDetailView,
    ProductUpdateView,
    ProductCreateView,
    ProductDeleteView,
)
from stock.views.stock import (
    ProductStockDeliveryTransfertCreateView,
    ProductStockReceptionTransfertCreateView,
    ProductStockDeliveryTransfertDeleteView,
    ProductStockReceptionTransfertDeleteView,
    ProductStockDeliveryTransfertUpdateView,
    ProductStockReceptionTransfertUpdateView,
    StockListView,
    StockListFilteredView,
    StockDetailDeliveryView,
    StockDetailReceptionView,
    StockUpdateView,
    StockCreateView,
    StockDeleteView,
    transfert_validate,
)


app_name = 'stock'

urlpatterns = [

    # Category CRUD
    re_path(r'^category/list/$', CategoryListView.as_view(),
            name="category-list"),
    re_path(r'^category/list/search/$', CategoryListFilteredView.as_view(),
            name="category-list-search"),
    re_path(r'^category/create/$', CategoryCreateView.as_view(),
            name="category-create"),
    re_path(r'^category/(?P<slug>[a-z0-9-]*)/update/$',
            CategoryUpdateView.as_view(), name="category-update"),
    re_path(r'^category/(?P<slug>[a-z0-9-]*)/delete/$',
            CategoryDeleteView.as_view(), name="category-delete"),

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
    re_path(r'^stock/list/$', StockListView.as_view(), name="stock-list"),
    re_path(r'^stock/list/search/$', StockListFilteredView.as_view(),
            name="stock-list-search"),
    re_path(r'^stock/create/$', StockCreateView.as_view(),
            name="stock-create"),
    re_path(r'^stock/(?P<slug>[a-z0-9-]*)/reception/$',
            StockDetailReceptionView.as_view(), name="stock-reception-detail"),
    re_path(r'^stock/(?P<slug>[a-z0-9-]*)/delivery/$',
            StockDetailDeliveryView.as_view(), name="stock-delivery-detail"),

    re_path(r'^stock/(?P<slug>[a-z0-9-]*)/update/$',
            StockUpdateView.as_view(), name="stock-update"),
    re_path(r'^stock/(?P<slug>[a-z0-9-]*)/delete/$',
            StockDeleteView.as_view(), name="stock-delete"),

    # ProductStockTransfert CRUD
    re_path(r'^stock/(?P<slug>[a-z0-9-]*)/delivery/transfert/create/$',
            ProductStockDeliveryTransfertCreateView.as_view(),
            name="delivery-transfert-create"),
    re_path(r'^stock/delivery/transfert/(?P<pk>\d+)update/$',
            ProductStockDeliveryTransfertUpdateView.as_view(), name="delivery-transfert-update"),
    re_path(r'^stock/delivery/transfert/(?P<pk>\d+)/delete/$',
            ProductStockDeliveryTransfertDeleteView.as_view(), name="delivery-transfert-delete"),

    re_path(r'^stock/(?P<slug>[a-z0-9-]*)/reception/transfert/create/$',
            ProductStockReceptionTransfertCreateView.as_view(),
            name="reception-transfert-create"),
    re_path(r'^stock/reception/transfert/(?P<pk>\d+)update/$',
            ProductStockReceptionTransfertUpdateView.as_view(), name="reception-transfert-update"),
    re_path(r'^stock/reception/transfert/(?P<pk>\d+)/delete/$',
            ProductStockReceptionTransfertDeleteView.as_view(), name="reception-transfert-delete"),
    re_path(r'^stock/reception/transfert/(?P<pk>\d+)/validate/$',
            transfert_validate, name="transfert-validate"),
]
