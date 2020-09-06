from django.urls import re_path
from django.contrib.auth import views as auth_views

from transaction.views.donation import (
    TransactionDonationCreateView,
    TransactionDonationDetailView,
    TransactionDonationDeleteView,
    TransactionDonationListView,
    TransactionListDonationFilteredView,
    TransactionDonationUpdateView,
)

from transaction.views.purchase import (
    TransactionPurchaseCreateView,
    TransactionPurchaseDetailView,
    TransactionPurchaseListView,
    TransactionListPurchaseFilteredView,
    TransactionPurchaseUpdateView,
    ProductTransactionPurchaseLineCreateView,
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
    re_path(r'^purchase/(?P<transaction_pk>\d+)/line/create/$',
            ProductTransactionPurchaseLineCreateView.as_view(), name="purchase-line-create")
]
