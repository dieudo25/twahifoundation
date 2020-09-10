from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from stock.models.category import Category


class CategoryResource(resources.ModelResource):
    """Describe how can model Category resources can be imported or exported"""

    class Meta:
        """Meta definition for CategoryResource."""

        model = Category
        skip_unchanged = True


class CategoryAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
