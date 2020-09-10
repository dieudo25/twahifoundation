from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from contact.models.person import Company


class CompanyResource(resources.ModelResource):
    """Describe how to can model Company resources can be imported or exported"""

    class Meta:
        """Meta definition for CompanyResource."""

        model = Company
        skip_unchanged = True


class CompanyAdmin(ImportExportModelAdmin):
    readonly_fields = ["slug"]
    resource_class = CompanyResource


admin.site.register(Company, CompanyAdmin)
