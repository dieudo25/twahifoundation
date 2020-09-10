from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from project.models.event import Event


class EventResource(resources.ModelResource):
    """Describe how can model Event resources can be imported or exported"""

    class Meta:
        """Meta definition for EventResource."""

        model = Event
        skip_unchanged = True


class EventAdmin(ImportExportModelAdmin):
    readonly_fields = ["slug"]
    resource_class = EventResource


admin.site.register(Event, EventAdmin)
