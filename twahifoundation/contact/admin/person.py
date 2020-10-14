from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from contact.models.person import Person


class PersonResource(resources.ModelResource):
    """Describe how Categomodel = Person resources can be imported or exported"""

    class Meta:
        """Meta definition for PersonResource."""

        model = Person
        skip_unchanged = True


class PersonAdmin(ImportExportModelAdmin):
    readonly_fields = ["slug"]
    resource_class = PersonResource
    ordering = ('first_name', 'last_name', 'email' )
    list_filter = ['is_deleted']
    list_display = ('first_name', 'last_name', 'email', 'is_deleted')
    search_fields = ['first_name', 'last_name', 'email',]


admin.site.register(Person, PersonAdmin)
