from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from project.models.task import Task


class TaskResource(resources.ModelResource):
    """Describe how can model Task resources can be imported or exported"""

    class Meta:
        """Meta definition for TaskResource."""

        model = Task
        skip_unchanged = True


class TaskAdmin(ImportExportModelAdmin):
    resource_class = TaskResource


admin.site.register(Task, TaskAdmin)
