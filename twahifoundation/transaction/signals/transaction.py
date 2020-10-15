from django.conf import settings
from django.core import mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from notifications.signals import notify

from account.models.user import User
from transaction.models.transaction import Transaction, ProductTransactionLine


@receiver(post_save, sender=Transaction)
def transaction_paypal_validated(sender, instance, created, **kwargs):

    if not created:
        send_to = []
        recipients = User.objects.filter(
            groups__name="Project manager")
        transaction = get_object_or_404(Transaction, pk=instance.pk)
        verb = 'made a donation'

        if transaction.with_paypal and transaction.is_valid:

            for recipient in recipients:
                notify.send(
                    instance.person,
                    recipient=recipient,
                    verb=verb,
                    action_object=instance
                )
                send_to.append(recipient.email)

            context = {
                'verb': verb,
                'user': instance.person,
            }
            subject = f'A new donation was made : { instance }'
            html_message = render_to_string(
                'portal/notification/email.html', context)
            plain_message = strip_tags(html_message)
            from_email = f'{ settings.EMAIL_HOST_USER }'

            mail.send_mail(subject, plain_message, from_email,
                           send_to, html_message=html_message)


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
