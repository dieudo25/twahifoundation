from django.contrib import admin

from blog.models.category import Category


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(Category, CategoryAdmin)
