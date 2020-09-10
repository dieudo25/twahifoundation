from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.signals import notify

from project.models.event import Event


@receiver(post_save, sender=Event)
def event_created_event(sender, instance, **kwargs):

    users = instance.users.all()
    notify.send(
        instance.created_by,
        recipient=users,
        verb='invite you to a new event',
        action_object=instance
    )
