from django.test import TestCase

from stock.models.category import Category
from stock.models.category import Category


class TestModels(TestCase):
    "Test Category Models"

    def setUp(self):
        "Set up Environnement for the test"

        self.category1 = Category.objects.create(
            name="Construction",
        )
