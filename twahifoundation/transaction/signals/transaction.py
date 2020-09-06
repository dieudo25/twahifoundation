from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from transaction.models.transaction import Transaction, ProductTransactionLine


@receiver(post_save, sender=ProductTransactionLine)
def create_update_transaction_line(sender, instance, **kwargs):

    total = 0
    transaction = Transaction.objects.get(id=instance.transaction.id)

    for line in transaction.producttransactionline_set.all():
        total += line.subtotal

    transaction.total = total
    transaction.save()


@receiver(post_delete, sender=ProductTransactionLine)
def delete_transaction_line(sender, instance, **kwargs):

    total = 0
    transaction = Transaction.objects.get(id=instance.transaction.id)

    for line in transaction.producttransactionline_set.all():
        total += line.subtotal

    transaction.total = total
    transaction.save()
