import json

from django.test import TestCase, Client
from django.urls import reverse

from stock.models.category import Category
from stock.models.product import Product


class TestViews(TestCase):
    "Test Product Views"

    def setUp(self):
        "Set up Environnement for the test"

        self.client = Client()

        self.list_url = reverse('stock:product-list')
        self.list_filtered_url = reverse('stock:product-list-search')
        self.detail_url = reverse(
            'stock:product-detail', args=['product-1'])
        self.update_url = reverse(
            'stock:product-update', args=['product-1'])
        self.create_url = reverse('stock:product-create')
        self.delete_url = reverse(
            'stock:product-delete', args=['product-1'])

        self.category1 = Category.objects.create(
            name="Construction",
        )

        self.product1 = Product.objects.create(
            name='Product 1',
            price=20,
            image="https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            description="Description of the product",
            is_saleable=True,
            is_purchasable=True,
            category=self.category1
        )

    def test_product_list(self):
        "Test VIEW ProductListView"

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/product/list.html')

    def test_product_list_filtered(self):
        "Test VIEW ProductListView FILTERED"

        response = self.client.get(self.list_filtered_url, {
            'search': 'Product 1'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/product/list.html')

    def test_product_detail(self):
        "Test VIEW ProductDetailView"

        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock/product/detail.html')

    def test_product_update(self):
        "Test VIEW ProductUpdateView"

        response = self.client.post(self.update_url, {
            'name': "Product 2",
            'image': "https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            'description': "description of the product uploadé",
            'price': 22,
            'is_saleable': True,
            'is_purchasable': False,
        })

        updated_product = Product.objects.filter(name="Product 2")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_product.count(), 1)

    def test_product_create(self):
        "Test VIEW ProductCreateView"

        response = self.client.post(self.create_url, {
            'name': "Product 3",
            'image': "https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            'description': "description of the product 3",
            'price': 214,
            'is_saleable': True,
            'is_purchasable': True,
        })

        product2 = Product.objects.get(name="Product 3")

        self.assertEqual(response.status_code, 302)
        self.assertEqual(product2.name, 'Product 3')

    def test_product_create_no_data(self):
        "Test VIEW ProductCreateView WITHOUT data"

        response = self.client.post(self.create_url)

        product3 = Product.objects.filter(name="Product 3").count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(product3, 0)
        self.assertTemplateUsed(response, 'stock/product/create.html')

    def test_product_delete(self):
        "Test VIEW ProductDeleteView"

        response = self.client.delete(self.delete_url, json.dumps({
            'id': 1
        }))

        products_number = Product.objects.all().count()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(products_number, 0)
