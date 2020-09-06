from django.contrib import admin

from blog.models.tags import Tags


class TagsAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(Tags, TagsAdmin)
