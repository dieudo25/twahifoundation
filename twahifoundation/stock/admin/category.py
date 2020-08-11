from django.contrib import admin

from stock.models.category import Category


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
