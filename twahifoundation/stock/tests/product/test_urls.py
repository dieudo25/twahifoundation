from django.test import SimpleTestCase
from django.urls import reverse, resolve

from stock.views.product import (
    ProductCreateView,
    ProductDeleteView,
    ProductListView,
    ProductListFilteredView,
    ProductDetailView,
    ProductUpdateView,
)


class TestUrls(SimpleTestCase):
    "Test stock app urls"

    # CRUD

    def test_product_list_url_resolves(self):
        "Test URL ProductListView"

        url = reverse('stock:product-list')
        self.assertEqual(resolve(url).func.__name__,
                         ProductListView.as_view().__name__)

    def test_product_list_filtered_url_resolves(self):
        "Test URL ProductListFilteredView"

        url = reverse('stock:product-list-search')
        self.assertEqual(resolve(url).func.__name__,
                         ProductListFilteredView.as_view().__name__)

    def test_product_detail_url_resolves(self):
        "Test URL ProductDetailView"

        url = reverse('stock:product-detail', args=['product1'])
        self.assertEqual(resolve(url).func.__name__,
                         ProductDetailView.as_view().__name__)

    def test_product_update_url_resolves(self):
        "Test URL ProductUpdateView"

        url = reverse('stock:product-update', args=['product1'])
        self.assertEqual(resolve(url).func.__name__,
                         ProductUpdateView.as_view().__name__)

    def test_product_create_url_resolves(self):
        "Test URL ProductCreateView"

        url = reverse('stock:product-create')
        self.assertEqual(resolve(url).func.__name__,
                         ProductCreateView.as_view().__name__)

    def test_product_delete_url_resolves(self):
        "Test URL ProductDeleteView"

        url = reverse('stock:product-delete', args=['product1'])
        self.assertEqual(resolve(url).func.__name__,
                         ProductDeleteView.as_view().__name__)
