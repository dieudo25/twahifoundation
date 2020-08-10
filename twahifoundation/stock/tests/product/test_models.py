from django.test import TestCase

from stock.models.product import Product
from stock.models.category import Category


class TestModels(TestCase):
    "Test Product Models"

    def setUp(self):
        "Set up Environnement for the test"

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

    def test_user_is_assigned_slug_on_creation(self):
        "Test if the slug is automatically genereted upon the object creation"

        self.assertEqual(self.product1.slug, 'product-1')
