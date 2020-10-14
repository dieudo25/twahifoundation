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

    ordering = ('title', 'created_by', 'date_created', 'date_ended' )
    list_filter = ['status', 'is_deleted']
    list_display = ('title', 'created_by', 'date_created', 'date_ended', 'status', 'is_deleted')
    search_fields = ['title', 'project', 'email',]


admin.site.register(Project, ProjectAdmin)
