from django.test import SimpleTestCase
from django.urls import reverse, resolve

from contact.views.company import (
    CompanyCreateView,
    CompanyDeleteView,
    CompanyListView,
    CompanyListFilteredView,
    CompanyDetailView,
    CompanyUpdateView,
)


class TestUrls(SimpleTestCase):
    "Test contact app urls"

    # CRUD

    def test_company_list_url_resolves(self):
        "Test URL CompanyListView"

        url = reverse('contact:company-list')
        self.assertEqual(resolve(url).func.__name__,
                         CompanyListView.as_view().__name__)

    def test_company_list_filtered_url_resolves(self):
        "Test URL CompanyListFilteredView"

        url = reverse('contact:company-list-search')
        self.assertEqual(resolve(url).func.__name__,
                         CompanyListFilteredView.as_view().__name__)

    """ def test_company_detail_url_resolves(self):
        "Test URL CompanyDetailView"

        url = reverse('contact:company-detail', args=['company1'])
        self.assertEqual(resolve(url).func.__name__,
                         CompanyDetailView.as_view().__name__)

    def test_company_update_url_resolves(self):
        "Test URL CompanyUpdateView"

        url = reverse('contact:company-update', args=['company1'])
        self.assertEqual(resolve(url).func.__name__,
                         CompanyUpdateView.as_view().__name__)

    def test_company_create_url_resolves(self):
        "Test URL CompanyCreateView"

        url = reverse('contact:company-create')
        self.assertEqual(resolve(url).func.__name__,
                         CompanyCreateView.as_view().__name__)

    def test_company_delete_url_resolves(self):
        "Test URL CompanyDeleteView"

        url = reverse('contact:company-delete', args=['company1'])
        self.assertEqual(resolve(url).func.__name__,
                         CompanyDeleteView.as_view().__name__) """
