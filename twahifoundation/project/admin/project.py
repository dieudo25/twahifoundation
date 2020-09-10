from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from project.models.project import Project


class ProjectResource(resources.ModelResource):
    """Describe how can model Project resources can be imported or exported"""

    class Meta:
        """Meta definition for ProjectResource."""

        model = Project
        skip_unchanged = True


class ProjectAdmin(ImportExportModelAdmin):
    readonly_fields = ["slug"]
    resource_class = ProjectResource


admin.site.register(Project, ProjectAdmin)
