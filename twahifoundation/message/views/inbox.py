from django.contrib.auth import get_user
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy

from message.models.message import Message

from message.forms.message import MessageCreateUpdateForm


class InboxListView(ListView):
    "Message list view"

    model = Message
    template_name = 'message/inbox/inbox.html'
    context_object_name = 'message_list'

    def get_queryset(self):
        """Get Message inbox list"""

        current_user = get_user(self.request)
        return Message.objects.inbox_for(current_user)


class InboxListFilteredView(ListView):
    "Message list filterd by title, location"

    model = Message
    template_name = 'message/inbox/inbox.html'
    context_object_name = 'filtered_message_list'

    def get_queryset(self):
        current_user = get_user(self.request)
        query = self.request.GET.get('search')
        object_list = Message.objects.filter(
            Q(recipient=current_user) |
            Q(recipient_deleted_at__isnull=True)
        ).filter(
            Q(sender__first_name__icontains=query) |
            Q(sender__last_name__icontains=query) |
            Q(recipient__first_name__icontains=query) |
            Q(recipient__last_name__icontains=query) |
            Q(subject__icontains=query)
        )
        return object_list


class InboxMessageDetailView(DetailView):
    "Message detail view"

    model = Message
    template_name = 'message/inbox/detail.html'
    context_object_name = 'message'


def inbox_to_trash(request, pk):
    "Place a message in the trash"

    message = Message.objects.get(pk=pk)
    message.recipient_delete()
    return redirect(reverse_lazy("message:message-inbox"))
