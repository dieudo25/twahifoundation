from django.contrib.auth.models import Group
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from notifications.signals import notify

from transaction.models.transaction import Transaction, ProductTransactionLine


@receiver(post_save, sender=Transaction)
def transaction_paypal_validated(sender, instance, created, **kwargs):

    if not created:
        transaction = get_object_or_404(Transaction, pk=instance.pk)

        if transaction.with_paypal and transaction.is_valid:
            recipient = Group.objects.get(name="Treasurer")
            notify.send(
                instance.person,
                recipient=recipient,
                verb='made a donation',
                action_object=instance
            )


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
