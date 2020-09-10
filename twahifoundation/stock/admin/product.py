from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from stock.models.product import Product


class ProductResource(resources.ModelResource):
    """Describe how can model Product resources can be imported or exported"""

    class Meta:
        """Meta definition for ProductResource."""

        model = Product
        skip_unchanged = True


class ProductAdmin(ImportExportModelAdmin):
    readonly_fields = ["slug"]
    resource_class = ProductResource


admin.site.register(Product, ProductAdmin)
