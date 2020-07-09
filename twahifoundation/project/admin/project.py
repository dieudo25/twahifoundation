from django.contrib import admin

from project.models.project import Project


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(Project, ProjectAdmin)
