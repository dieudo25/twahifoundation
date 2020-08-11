from django.test import TestCase

from stock.models.category import Category
from stock.forms.category import CategoryCreateUpdateForm


class TestForms(TestCase):
    "Test Event forms"

    def test_category_create_update_form_valid_data(self):
        "Test thee validation of the the data upon creation or update of the category"

        form = CategoryCreateUpdateForm(data={
            'name': "Category 1",
        })

        self.assertTrue(form.is_valid())

    def test_category_create_update_form_no_valid(self):
        ""

        form = CategoryCreateUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
