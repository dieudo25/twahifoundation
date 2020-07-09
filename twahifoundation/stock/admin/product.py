from django.contrib import admin

from stock.models.product import Product


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["slug"]


admin.site.register(Product, ProductAdmin)
