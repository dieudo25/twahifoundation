import json

from django.test import TestCase, Client
from django.urls import reverse

from contact.models.company import Company


class TestViews(TestCase):
    "Test Company Views"

    def setUp(self):
        "Set up Environnement for the test"

        self.client = Client()

        self.list_url = reverse('contact:company-list')
        self.list_filtered_url = reverse('contact:company-list-search')
        self.detail_url = reverse(
            'contact:company-detail', args=['proximus'])
        self.update_url = reverse(
            'contact:company-update', args=['proximus'])
        self.create_url = reverse('contact:company-create')
        self.delete_url = reverse(
            'contact:company-delete', args=['proximus'])

        self.company1 = Company.objects.create(
            name='Proximus',
            email="proximusM@gmail.com",
            phone_number="0476543298",
            is_partner=True,
            address="Avenue Marie de Hongrie 67 1083 Ganshoren",
            website="www.proximus.com",
        )

    def test_company_list(self):
        "Test VIEW CompanyListView"

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/company/list.html')

    def test_company_list_filtered(self):
        "Test VIEW CompanyListView FILTERED"

        response = self.client.get(self.list_filtered_url, {
            'search': 'Proximus'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/company/list_filtered.html')

    def test_company_detail(self):
        "Test VIEW CompanyDetailView"

        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/company/detail.html')

    def test_company_updtae(self):
        "Test VIEW CompanyUpdateView"

        response = self.client.post(self.update_url, {
            'name': 'Orange',
            'email': 'orange@gmail.com',
            'phone_number': '9677687698',
            'is_partner': True,
            'website': "www.orange.be",
            'address': "Avenue de la pègre 12 1090 Jette",
        })

        updated_company = Company.objects.filter(name="Orange")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_company.count(), 1)

    def test_company_create(self):
        "Test VIEW CompanyCreateView"

        response = self.client.post(self.create_url, {
            'name': 'MediaMarkt',
            'email': 'fontel@gmail.com',
            'phone_number': '97754556',
            'address': 'Rue de la Fontaine 345 1000 Bruxelles',
            'website': 'https://www.mediamarkt.be',
            'is_partner': True,
        })

        company2 = Company.objects.get(name="MediaMarkt")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(company2.name, 'MediaMarkt')

    def test_company_create_no_data(self):
        "Test VIEW CompanyCreateView WITHOUT data"

        response = self.client.post(self.create_url)

        company3 = Company.objects.filter(name="Vans").count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(company3, 0)
        self.assertTemplateUsed(response, 'contact/company/create.html')

    def test_company_delete(self):
        "Test VIEW CompanyDeleteView"

        response = self.client.delete(self.delete_url, json.dumps({
            'id': 1
        }))

        companies_number = Company.objects.all().count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(companies_number, 0)
