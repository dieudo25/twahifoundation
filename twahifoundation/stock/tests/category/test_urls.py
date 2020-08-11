from django.test import SimpleTestCase
from django.urls import reverse, resolve

from stock.views.category import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryListView,
    CategoryListFilteredView,
    CategoryUpdateView,
)


class TestUrls(SimpleTestCase):
    "Test stock app urls"

    # CRUD

    def test_category_list_url_resolves(self):
        "Test URL CategoryListView"

        url = reverse('stock:category-list')
        self.assertEqual(resolve(url).func.__name__,
                         CategoryListView.as_view().__name__)

    def test_category_list_filtered_url_resolves(self):
        "Test URL CategoryListFilteredView"

        url = reverse('stock:category-list-search')
        self.assertEqual(resolve(url).func.__name__,
                         CategoryListFilteredView.as_view().__name__)

    def test_category_update_url_resolves(self):
        "Test URL CategoryUpdateView"

        url = reverse('stock:category-update', args=['category1'])
        self.assertEqual(resolve(url).func.__name__,
                         CategoryUpdateView.as_view().__name__)

    def test_category_create_url_resolves(self):
        "Test URL CategoryCreateView"

        url = reverse('stock:category-create')
        self.assertEqual(resolve(url).func.__name__,
                         CategoryCreateView.as_view().__name__)

    def test_category_delete_url_resolves(self):
        "Test URL CategoryDeleteView"

        url = reverse('stock:category-delete', args=['category1'])
        self.assertEqual(resolve(url).func.__name__,
                         CategoryDeleteView.as_view().__name__)
