from django.conf import settings
from django.core import mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from notifications.signals import notify

from message.models.message import Message


@receiver(post_save, sender=Message)
def message_sent_event(sender, instance, created, **kwargs):

    if created:
        send_to = []
        recipient = instance.recipient
        verb = 'sent you a message'
        notify.send(
            instance.sender,
            recipient=recipient,
            verb=verb,
            action_object=instance
        )
        send_to.append(instance.recipient.email)

        context = {
            'verb': verb,
            'user': instance.sender,
        }
        subject = f'{ instance.subject }'
        html_message = render_to_string(
            'portal/notification/email.html', context)
        plain_message = strip_tags(html_message)
        from_email = f'{ settings.EMAIL_HOST_USER }'

        mail.send_mail(subject, plain_message, from_email,
                       send_to, html_message=html_message)
