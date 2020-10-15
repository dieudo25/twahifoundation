from django.conf import settings
from django.core import mail
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from notifications.signals import notify

from account.models.user import User
from project.models.event import Event


@receiver(post_save, sender=Event)
def event_created(sender, instance, created, **kwargs):

    if created:
        send_to = []
        recipients = User.objects.filter(
            groups__name="Member").exclude(id=instance.created_by.id)
        verb = 'invite you to a new event'

        for recipient in recipients:
            notify.send(
                instance.created_by,
                recipient=recipient,
                verb=verb,
                action_object=instance
            )
            send_to.append(recipient.email)

        """ context = {
            'verb': verb,
            'user': instance.created_by,
        }
        subject = f'A New event was created : { instance.title }'
        html_message = render_to_string(
            'portal/notification/email.html', context)
        plain_message = strip_tags(html_message)
        from_email = f'{ settings.EMAIL_HOST_USER }'

        mail.send_mail(subject, plain_message, from_email,
                       send_to, html_message=html_message) """


@receiver(m2m_changed, sender=Event.users.through)
def task_user(sender, instance, action, pk_set, ** kwargs):

    if action == 'pre_add':
        send_to = []
        recipients = instance.users.all()
        verb = 'participates at the event'

        for user_pk in pk_set:
            new_participant = get_object_or_404(User, pk=user_pk)

            for recipient in recipients:
                notify.send(
                    new_participant,
                    recipient=recipient,
                    verb=verb,
                    action_object=instance
                )
                send_to.append(recipient.email)

            context = {
                'verb': verb,
                'user': new_participant,
            }
            subject = f'The event "{ instance.title }" have a new participant'
            html_message = render_to_string(
                'portal/notification/email.html', context)
            plain_message = strip_tags(html_message)
            from_email = f'{ settings.EMAIL_HOST_USER }'

            mail.send_mail(subject, plain_message, from_email,
                           send_to, html_message=html_message)

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
