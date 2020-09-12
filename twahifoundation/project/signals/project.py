from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.signals import notify

from project.models.project import Project


@receiver(post_save, sender=Project)
def project_created(sender, instance, created, **kwargs):

    if created:
        recipient = Group.objects.get(name="Member")
        notify.send(
            instance.created_by,
            recipient=recipient,
            verb='created a new project',
            action_object=instance
        )
