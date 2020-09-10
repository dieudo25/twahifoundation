from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from message.models.message import Message


class MessageResource(resources.ModelResource):
    """Describe how can model Message resources can be imported or exported"""

    class Meta:
        """Meta definition for MessageResource."""

        model = Message
        skip_unchanged = True


class MessageAdmin(ImportExportModelAdmin):

    readonly_fields = ["slug"]
    resource_class = MessageResource


admin.site.register(Message, MessageAdmin)
