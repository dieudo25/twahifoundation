from django.urls import re_path
from django.contrib.auth import views as auth_views

from transaction.views.transaction import (
    TransactionCreateView,
    TransactionDetailView,
    TransactionDeleteView,
    TransactionDonationListView,
    TransactionListDonationFilteredView,
    TransactionSaleListView,
    TransactionListSaleFilteredView,
    TransactionPurchaseListView,
    TransactionListPurchaseFilteredView,
    TransactionUpdateView,
)

app_name = 'transaction'

urlpatterns = [
    re_path(r'^transaction/list/$', TransactionDonationListView.as_view(),
            name="transaction-donation-list"),
    re_path(r'^transaction/list/search/$', TransactionListDonationFilteredView.as_view(),
            name="transaction-donation-list-search"),
    re_path(r'^transaction/create/$', TransactionCreateView.as_view(),
            name="transaction-create"),
    re_path(r'^transaction/(?P<pk>\d+)/$',
            TransactionDetailView.as_view(), name="transaction-detail"),
    re_path(r'^transaction/(?P<pk>\d+)/update/$',
            TransactionUpdateView.as_view(), name="transaction-update"),

    re_path(r'^transaction/(?P<pk>\d+)/delete/$',
            TransactionDeleteView.as_view(), name="transaction-delete"),
]
