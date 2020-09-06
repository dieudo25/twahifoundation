from django.db.models.signals import post_save
from django.dispatch import receiver

from transaction.models.transaction import Transaction, ProductTransactionLine


@receiver(post_save, sender=ProductTransactionLine)
def update_transaction(sender, instance, created, **kwargs):

    total = 0
    transaction = Transaction.objects.get(id=instance.transaction.id)

    for line in transaction.producttransactionline_set.all():
        total += line.subtotal

    transaction.total = total
    transaction.save()
