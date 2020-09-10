from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from blog.models.category import Category


class CategoryResource(resources.ModelResource):
    """Describe how can model Category resources can be imported or exported"""

    class Meta:
        """Meta definition for CategoryResource."""

        model = Category
        skip_unchanged = True


class CategoryAdmin(ImportExportModelAdmin):
    readonly_fields = ["slug"]
    resource_class = CategoryResource


admin.site.register(Category, CategoryAdmin)
