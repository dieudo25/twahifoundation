from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.signals import notify

from blog.models.post import Post


@receiver(post_save, sender=Post)
def event_created(sender, instance, created, **kwargs):

    if created:
        verb = ''

        if instance.category.name == 'Post':
            verb = 'created a new post'
        else:
            verb = 'created a new page'

        recipient = Group.objects.get(name="Project manager")
        notify.send(
            instance.user,
            recipient=recipient,
            verb=verb,
            action_object=instance
        )
    else:
        if instance.category.name == 'Post':
            verb = 'updated a post'
        else:
            verb = 'updated a page'

        recipient = Group.objects.get(name="Project manager")
        notify.send(
            instance.user,
            recipient=recipient,
            verb=verb,
            action_object=instance
        )
