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

    ordering = ('name', 'price', 'quantity', )
    list_filter = ['is_saleable', 'is_purchasable', 'is_deleted']
    list_display = ('name', 'price', 'quantity', 'is_saleable', 'is_purchasable', 'is_deleted')
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
