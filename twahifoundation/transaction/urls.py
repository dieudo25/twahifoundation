from django.urls import re_path
from django.contrib.auth import views as auth_views

from transaction.views.donation import (
    TransactionDonationCreateView,
    TransactionDonationDetailView,
    TransactionDonationDeleteView,
    TransactionDonationListView,
    TransactionListDonationFilteredView,
    TransactionDonationUpdateView,
    donation_validate,
)

from transaction.views.purchase import (
    TransactionPurchaseCreateView,
    TransactionPurchaseDetailView,
    TransactionPurchaseListView,
    TransactionListPurchaseFilteredView,
    TransactionPurchaseUpdateView,
    ProductTransactionPurchaseLineCreateView,
    ProductTransactionPurchaseLineDeleteView,
    ProductTransactionPurchaseLineUpdateView,
    purchase_validate,
)

from transaction.views.sale import (
    TransactionSaleCreateView,
    TransactionSaleDetailView,
    TransactionSaleListView,
    TransactionListSaleFilteredView,
    TransactionSaleUpdateView,
    ProductTransactionSaleLineCreateView,
    ProductTransactionSaleLineDeleteView,
    ProductTransactionSaleLineUpdateView,
    sale_validate,
)

app_name = 'transaction'

urlpatterns = [

    # Donation
    re_path(r'^donation/list/$', TransactionDonationListView.as_view(),
            name="donation-list"),
    re_path(r'^donation/list/search/$', TransactionListDonationFilteredView.as_view(),
            name="donation-list-search"),
    re_path(r'^donation/create/$', TransactionDonationCreateView.as_view(),
            name="donation-create"),
    re_path(r'^donation/(?P<pk>\d+)/$',
            TransactionDonationDetailView.as_view(), name="donation-detail"),
    re_path(r'^donation/(?P<pk>\d+)/update/$',
            TransactionDonationUpdateView.as_view(), name="donation-update"),

    re_path(r'^donation/(?P<pk>\d+)/delete/$',
            TransactionDonationDeleteView.as_view(), name="donation-delete"),
    re_path(r'^donation/(?P<pk>\d+)/validate/$',
            donation_validate, name="donation-validate"),

    # Purchase
    re_path(r'^purchase/list/$', TransactionPurchaseListView.as_view(),
            name="purchase-list"),
    re_path(r'^purchase/list/search/$', TransactionListPurchaseFilteredView.as_view(),
            name="purchase-list-search"),
    re_path(r'^purchase/create/$', TransactionPurchaseCreateView.as_view(),
            name="purchase-create"),
    re_path(r'^purchase/(?P<pk>\d+)/$',
            TransactionPurchaseDetailView.as_view(), name="purchase-detail"),
    re_path(r'^purchase/(?P<pk>\d+)/update/$',
            TransactionPurchaseUpdateView.as_view(), name="purchase-update"),
    re_path(r'^purchase/(?P<pk>\d+)/delete/$',
            TransactionDonationDeleteView.as_view(), name="purchase-delete"),
    re_path(r'^purchase/(?P<pk>\d+)/validate/$',
            purchase_validate, name="purchase-validate"),

    # Transaction Purchase Line
    re_path(r'^purchase/(?P<transaction_pk>\d+)/line/create/$',
            ProductTransactionPurchaseLineCreateView.as_view(), name="purchase-line-create"),
    re_path(r'^purchase/line/(?P<pk>\d+)delete/$',
            ProductTransactionPurchaseLineDeleteView.as_view(), name="purchase-line-delete"),
    re_path(r'^purchase/line/(?P<pk>\d+)update/$',
            ProductTransactionPurchaseLineUpdateView.as_view(), name="purchase-line-update"),

    # Sale
    re_path(r'^sale/list/$', TransactionSaleListView.as_view(),
            name="sale-list"),
    re_path(r'^sale/list/search/$', TransactionListSaleFilteredView.as_view(),
            name="sale-list-search"),
    re_path(r'^sale/create/$', TransactionSaleCreateView.as_view(),
            name="sale-create"),
    re_path(r'^sale/(?P<pk>\d+)/$',
            TransactionSaleDetailView.as_view(), name="sale-detail"),
    re_path(r'^sale/(?P<pk>\d+)/update/$',
            TransactionSaleUpdateView.as_view(), name="sale-update"),
    re_path(r'^sale/(?P<pk>\d+)/delete/$',
            TransactionDonationDeleteView.as_view(), name="sale-delete"),
    re_path(r'^sale/(?P<pk>\d+)/validate/$',
            sale_validate, name="sale-validate"),

    # Transaction Sale Line
    re_path(r'^sale/(?P<transaction_pk>\d+)/line/create/$',
            ProductTransactionSaleLineCreateView.as_view(), name="sale-line-create"),
    re_path(r'^sale/line/(?P<pk>\d+)delete/$',
            ProductTransactionSaleLineDeleteView.as_view(), name="sale-line-delete"),
    re_path(r'^sale/line/(?P<pk>\d+)update/$',
            ProductTransactionSaleLineUpdateView.as_view(), name="sale-line-update"),
]
