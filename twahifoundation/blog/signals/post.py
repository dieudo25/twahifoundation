from django.conf import settings
from django.core import mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from notifications.signals import notify

from account.models.user import User
from blog.models.post import Post


@receiver(post_save, sender=Post)
def event_created(sender, instance, created, **kwargs):

    recipients = User.objects.filter(
        groups__name="Project manager").exclude(id=instance.user.id)
    verb = ''
    subject = ''

    if created:
        send_to = []

        if instance.category.name == 'Post':
            verb = 'created a new post'
            subject = f'A new post created : { instance.title }'
        else:
            verb = 'created a new page'
            subject = f'A new page created : { instance.title }'

        for recipient in recipients:
            notify.send(
                instance.user,
                recipient=recipient,
                verb=verb,
                action_object=instance
            )
            send_to.append(recipient.email)

        context = {
            'verb': verb,
            'user': instance.user,
        }
        html_message = render_to_string(
            'portal/notification/email.html', context)
        plain_message = strip_tags(html_message)
        from_email = f'{ settings.EMAIL_HOST_USER }'

        mail.send_mail(subject, plain_message, from_email,
                       send_to, html_message=html_message)

    else:
        send_to = []

        if instance.category.name == 'Post':
            verb = 'updated a post'
            subject = f'The post { instance.title } : was updated'
        else:
            verb = 'updated a page'
            subject = f'The page { instance.title } : was updated'

        for recipient in recipients:
            notify.send(
                instance.user,
                recipient=recipient,
                verb=verb,
                action_object=instance
            )
            send_to.append(recipient.email)

        context = {
            'verb': verb,
            'user': instance.user,
        }
        html_message = render_to_string(
            'portal/notification/email.html', context)
        plain_message = strip_tags(html_message)
        from_email = f'{ settings.EMAIL_HOST_USER }'

        mail.send_mail(subject, plain_message, from_email,
                       send_to, html_message=html_message)
        print(mail.send_mail(subject, plain_message, from_email,
                             send_to, html_message=html_message))
