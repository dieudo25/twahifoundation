import itertools

from django.conf import settings
from django.db import models
from django.db.models import signals
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class MessageManager(models.Manager):

    def inbox_for(self, user):
        """
        Returns all messages that were received by the given user and are not
        marked as deleted.
        """
        return self.filter(
            recipient=user,
            recipient_deleted_at__isnull=True,
        )

    def outbox_for(self, user):
        """
        Returns all messages that were sent by the given user and are not
        marked as deleted.
        """
        return self.filter(
            sender=user,
            sender_deleted_at__isnull=True,
        )

    def trash_for(self, user):
        """
        Returns all messages that were either received or sent by the given
        user and are marked as deleted.
        """
        return self.filter(
            recipient=user,
            recipient_deleted_at__isnull=False,
        ) | self.filter(
            sender=user,
            sender_deleted_at__isnull=False,
        )


class Message(models.Model):
    """
    A private message from user to user
    """
    subject = models.CharField(_("Subject"), max_length=140)
    body = RichTextUploadingField()
    sender = models.ForeignKey(AUTH_USER_MODEL, related_name='sent_messages', verbose_name=_(
        "Sender"), on_delete=models.PROTECT)
    recipient = models.ForeignKey(AUTH_USER_MODEL, related_name='received_messages',
                                  null=True, blank=True, verbose_name=_("Recipient"), on_delete=models.SET_NULL)
    parent_msg = models.ForeignKey('self', related_name='next_messages', null=True,
                                   blank=True, verbose_name=_("Parent message"), on_delete=models.SET_NULL)
    sent_at = models.DateTimeField(_("sent at"), null=True, blank=True)
    read_at = models.DateTimeField(_("read at"), null=True, blank=True)
    replied_at = models.DateTimeField(_("replied at"), null=True, blank=True)
    sender_deleted_at = models.DateTimeField(
        _("Sender deleted at"), null=True, blank=True)
    recipient_deleted_at = models.DateTimeField(
        _("Recipient deleted at"), null=True, blank=True)
    uploaded_file = models.FileField(
        upload_to='messages/%Y/%m/%D',
        max_length=100,
        blank=True,
        null=True
    )
    slug = models.SlugField(max_length=60, unique=True)
    sender_delete_once = models.BooleanField(default=False)
    recipient_delete_once = models.BooleanField(default=False)

    objects = MessageManager()

    def _generate_slug(self):
        """
        Generate a slug based on the title of the project

        If the slug is already taken, one or two digits will be added at the
        end of the slug and will increment as long as the slug already exist
        until reaching a non-existant result.
        The slug is truncated to 57 character in order to add the unique digits
        at the end of it.
        """

        max_length = self._meta.get_field('slug').max_length - 3
        value = self.subject
        slug_result = slug_original = \
            slugify(value, allow_unicode=False)[:max_length]

        for i in itertools.count(1):
            if not Message.objects.filter(slug=slug_result).exists():
                break
            slug_result = f'{slug_original}-{i}'

        self.slug = slug_result

    def new(self):
        """returns whether the recipient has read the message or not"""
        if self.read_at is not None:
            return False
        return True

    def replied(self):
        """returns whether the recipient has written a reply to this message"""
        if self.replied_at is not None:
            return True
        return False

    def read(self):
        """instanciate read_at field with now"""

        self.read_at = timezone.now()
        self.save()

    def __str__(self):
        return self.subject

    def sender_delete(self):
        "Sender delete message into the trash"

        self.sender_deleted_at = timezone.now()
        self.save()

    def recipient_delete(self):
        "Recipient delete message into the trash"

        self.recipient_deleted_at = timezone.now()
        self.save()

    def sender_restore(self):
        "Sender Restore a message from the trash"

        self.sender_deleted_at = None
        self.save()

    def recipient_restore(self):
        "Recipient Restore a message from the trash"

        self.recipient_deleted_at = None
        self.save()

    def sender_deleted_once(self):
        "Delete the message once in safe mode"

        self.sender_delete_once = True
        self.save()

    def recipient_deleted_once(self):
        "Delete the message once in safe mode"

        self.recipient_delete_once = True
        self.save()

    def save(self, **kwargs):

        if not self.pk:
            self._generate_slug()
            self.sent_at = timezone.now()

        super(Message, self).save(**kwargs)

    class Meta:
        ordering = ['-sent_at']
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")


def inbox_count_for(user):
    """
    returns the number of unread messages for the given user but does not
    mark them seen
    """
    return Message.objects.filter(recipient=user, read_at__isnull=True, recipient_deleted_at__isnull=True).count()
