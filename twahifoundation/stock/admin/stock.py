from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from stock.models.stock import Stock, ProductStockTransfert


class ProductStockTransfertInline(admin.TabularInline):
    model = ProductStockTransfert
    extra = 0
    readonly_fields = ['date_time_created']


class StockResource(resources.ModelResource):
    """Describe how can model Stock resources can be imported or exported"""

    class Meta:
        """Meta definition for StockResource."""

        model = Stock
        skip_unchanged = True


class StockAdmin(ImportExportModelAdmin):
    model = Stock
    inlines = [ProductStockTransfertInline, ]
    resource_class = StockResource

    ordering = ('name', 'location', 'date_created', )
    list_filter = ['is_full']
    list_display = ('name', 'location', 'date_created', 'is_full',)
    search_fields = ['is_full']


admin.site.register(Stock, StockAdmin)
