from django.test import TestCase

from stock.models.product import Product
from stock.forms.product import ProductCreateUpdateForm


class TestForms(TestCase):
    "Test Event forms"

    def test_product_create_update_form_valid_data(self):
        "Test thee validation of the the data upon creation or update of the product"

        form = ProductCreateUpdateForm(data={
            'name': "Product 1",
            'image': "https://www.optoma.fr/images/ProductApplicationFeatures/4kuhd/banner.jpg",
            'description': "description of the product",
            'price': 20,
            'is_saleable': True,
            'is_purchasable': True,

        })

        self.assertTrue(form.is_valid())

    def test_product_create_update_form_no_valid(self):
        ""

        form = ProductCreateUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
