from django.contrib.auth import get_user
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy

from message.models.message import Message

from message.forms.message import MessageCreateUpdateForm


class OutboxListView(ListView):
    "Message list view"

    model = Message
    template_name = 'message/outbox/outbox.html'
    context_object_name = 'message_list'

    def get_queryset(self):
        """Get message outbox list"""

        current_user = get_user(self.request)
        return Message.objects.outbox_for(current_user)


class OutboxListFilteredView(ListView):
    "Message list filterd by title, location"

    model = Message
    template_name = 'message/outbox/outbox.html'
    context_object_name = 'filtered_message_list'

    def get_queryset(self):
        current_user = get_user(self.request)
        query = self.request.GET.get('search')
        object_list = Message.objects.filter(
            Q(sender=current_user) |
            Q(sender_deleted_at__isnull=True)
        ).filter(
            Q(sender__first_name__icontains=query) |
            Q(sender__last_name__icontains=query) |
            Q(recipient__first_name__icontains=query) |
            Q(recipient__last_name__icontains=query) |
            Q(subject__icontains=query)
        )
        return object_list


class OutboxMessageDetailView(DetailView):
    "Message detail view"

    model = Message
    template_name = 'message/outbox/detail.html'
    context_object_name = 'message'


def outbox_to_trash(request, pk):
    "Place a message in the trash"

    message = Message.objects.get(pk=pk)
    message.sender_delete()
    return redirect(reverse_lazy("message:outbox"))
