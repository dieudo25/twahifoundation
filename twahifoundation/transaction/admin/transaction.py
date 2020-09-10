from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from transaction.models.transaction import Transaction, ProductTransactionLine


class ProductTransactionLineInline(admin.TabularInline):
    model = ProductTransactionLine
    extra = 1
    readonly_fields = ['sous_total']

    def sous_total(self, obj):
        return str(obj.quantity * obj.product.price) + "€"


class TransactionResource(resources.ModelResource):
    """Describe how can model Transaction resources can be imported or exported"""

    class Meta:
        """Meta definition for TransactionResource."""

        model = Transaction
        skip_unchanged = True


class TransactionAdmin(ImportExportModelAdmin):
    model = Transaction
    inlines = [ProductTransactionLineInline]
    readonly_fields = ['total']

    def total(self, obj):
        """
        Fonction that return the total price of the purchasing transaction
        """

        total = 0

        for transaction_line in obj.producttransactionline_set.all():
            total += transaction_line.product.price * transaction_line.quantity
        return str(total) + "€"


admin.site.register(Transaction, TransactionAdmin)
