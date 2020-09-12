from django.contrib.auth.models import Group
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from notifications.models import Notification
from notifications.signals import notify

from account.models.user import User
from project.models.task import Task


@receiver(m2m_changed, sender=Task.users.through)
def task_user(sender, instance, action, pk_set, ** kwargs):

    if action == 'post_add':
        users = {}
        for pk in pk_set:
            user = User.objects.get(pk=pk)
            users[pk] = user

        for recipient in users.values():
            notify.send(
                instance.created_by,
                recipient=recipient,
                verb='assigned you a new task',
                action_object=instance
            )

    if action == 'post_remove':
        users = {}
        for pk in pk_set:
            user = User.objects.get(pk=pk)
            users[pk] = user

        for recipient in users.values():
            notice = recipient.notifications.unread()
            notice.delete()
