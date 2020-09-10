from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from blog.models.post import Post


class PostResource(resources.ModelResource):
    """Describe how can model Post resources can be imported or exported"""

    class Meta:
        """Meta definition for PostResource."""

        model = Post
        skip_unchanged = True


class PostAdmin(ImportExportModelAdmin):
    readonly_fields = ["slug"]
    resource_class = PostResource


admin.site.register(Post, PostAdmin)
