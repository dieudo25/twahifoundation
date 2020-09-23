from django.conf import settings
from django.core import mail
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from notifications.signals import notify

from account.models.user import User
from project.models.task import Task


@receiver(m2m_changed, sender=Task.users.through)
def task_user(sender, instance, action, pk_set, ** kwargs):

    if action == 'post_add':
        send_to = []
        users = {}
        verb = 'assigned you a new task'

        for pk in pk_set:
            user = User.objects.get(pk=pk)
            users[pk] = user

        for recipient in users.values():
            notify.send(
                instance.created_by,
                recipient=recipient,
                verb=verb,
                action_object=instance
            )
            send_to.append(recipient.email)

        context = {
            'verb': verb,
            'user': instance.created_by,
        }
        subject = f'You have been assigned a new task : { instance.title }'
        html_message = render_to_string(
            'portal/notification/email.html', context)
        plain_message = strip_tags(html_message)
        from_email = f'{ settings.EMAIL_HOST_USER }'

        mail.send_mail(subject, plain_message, from_email,
                       send_to, html_message=html_message)

    if action == 'pre_remove':
        users = {}
        for pk in pk_set:
            user = User.objects.get(pk=pk)
            users[pk] = user

        for recipient in users.values():
            notifications = recipient.notifications.unread()

            for notice in notifications:

                if notice.action_object.slug == instance.slug:
                    notice.delete()
