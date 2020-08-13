from django.contrib import admin

from stock.models.stock import Stock, ProductStockTransfert


class ProductStockTransfertInline(admin.TabularInline):
    model = ProductStockTransfert
    extra = 0
    readonly_fields = ['date_created']


class StockAdmin(admin.ModelAdmin):
    model = Stock
    inlines = [ProductStockTransfertInline, ]


admin.site.register(Stock, StockAdmin)
