from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.signals import notify

from project.models.event import Event


@receiver(post_save, sender=Event)
def event_created(sender, instance, created, **kwargs):

    if created:
        recipient = Group.objects.get(name="Member")
        notify.send(
            instance.created_by,
            recipient=recipient,
            verb='invite you to a new event',
            action_object=instance
        )
