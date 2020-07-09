from django.contrib import admin

from stock.models.stock import Stock


class StockAdmin(admin.ModelAdmin):
    pass


admin.site.register(Stock, StockAdmin)
