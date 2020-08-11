import json

from django.test import TestCase, Client
from django.urls import reverse

from stock.models.category import Category
from stock.models.category import Category


class TestViews(TestCase):
    "Test Category Views"

    def setUp(self):
        "Set up Environnement for the test"

        self.client = Client()

        self.list_url = reverse('stock:category-list')
        self.list_filtered_url = reverse('stock:category-list-search')
        self.update_url = reverse(
            'stock:category-update', args=['category-1'])
        self.create_url = reverse('stock:category-create')
        self.delete_url = reverse(
            'stock:category-delete', args=['category-1'])

        self.category1 = Category.objects.create(
            name="Category 1",
        )

    def test_category_list(self):
        "Test VIEW CategoryListView"

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/category/list.html')

    def test_category_list_filtered(self):
        "Test VIEW CategoryListView FILTERED"

        response = self.client.get(self.list_filtered_url, {
            'search': 'Category 1'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/category/list.html')

    def test_category_update(self):
        "Test VIEW CategoryUpdateView"

        response = self.client.post(self.update_url, {
            'name': "Category 2",
        })

        updated_category = Category.objects.filter(name="Category 2")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_category.count(), 1)

    def test_category_create(self):
        "Test VIEW CategoryCreateView"

        response = self.client.post(self.create_url, {
            'name': "Category 3",
        })

        category2 = Category.objects.get(name="Category 3")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(category2.name, 'Category 3')

    def test_category_create_no_data(self):
        "Test VIEW CategoryCreateView WITHOUT data"

        response = self.client.post(self.create_url)

        category3 = Category.objects.filter(name="Category 3").count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(category3, 0)
        self.assertTemplateUsed(response, 'stock/category/create.html')

    def test_category_delete(self):
        "Test VIEW CategoryDeleteView"

        response = self.client.delete(self.delete_url, json.dumps({
            'id': 1
        }))

        categorys_number = Category.objects.all().count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(categorys_number, 0)
