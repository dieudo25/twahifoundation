from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.signals import notify

from account.models.user import User
from project.models.project import Project


@receiver(post_save, sender=Project)
def project_created(sender, instance, created, **kwargs):

    if created:
        recipients = User.objects.filter(
            groups__name="Member").exclude(id=instance.created_by.id)

        for recipient in recipients:
            notify.send(
                instance.created_by,
                recipient=recipient,
                verb='created a new project',
                action_object=instance
            )
