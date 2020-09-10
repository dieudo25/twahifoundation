from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from blog.models.tags import Tags


class TagsResource(resources.ModelResource):
    """Describe how can model Tags resources can be imported or exported"""

    class Meta:
        """Meta definition for TagsResource."""

        model = Tags
        skip_unchanged = True


class TagsAdmin(ImportExportModelAdmin):
    readonly_fields = ["slug"]
    resource_class = TagsResource


admin.site.register(Tags, TagsAdmin)
