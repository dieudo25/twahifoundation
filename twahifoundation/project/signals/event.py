from django.contrib.auth.models import Group
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from notifications.signals import notify

from account.models.user import User
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


@receiver(m2m_changed, sender=Event.users.through)
def task_user(sender, instance, action, pk_set, ** kwargs):

    if action == 'pre_add':
        for user_pk in pk_set:
            new_participant = get_object_or_404(User, pk=user_pk)

            for recipient in instance.users.all():
                notify.send(
                    new_participant,
                    recipient=recipient,
                    verb='participates at the event',
                    action_object=instance
                )

    if action == 'pre_remove':
        users = {}

        for pk in pk_set:
            user = get_object_or_404(User, pk=pk)
            users[pk] = user

        for recipient in instance.users.all():
            notifications = recipient.notifications.unread()

            for notice in notifications:

                if notice.actor in users.values():

                    if notice.verb == 'participates at the event':

                        if notice.action_object.slug == instance.slug:
                            notice.delete()
