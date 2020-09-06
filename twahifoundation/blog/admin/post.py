from django.contrib import admin

from blog.models.post import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(Post, PostAdmin)
