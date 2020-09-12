from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.signals import notify

from message.models.message import Message


@receiver(post_save, sender=Message)
def message_sent_event(sender, instance, **kwargs):

    recipient = instance.recipient
    notify.send(
        instance.sender,
        recipient=recipient,
        verb='sent you a message',
        action_object=instance
    )
