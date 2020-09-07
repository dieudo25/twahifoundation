from django.contrib import auth
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy

from message.models.message import Message

from message.forms.message import MessageCreateUpdateForm


class TrashListView(ListView):
    "Message list view"

    model = Message
    template_name = 'message/trash/trash.html'
    context_object_name = 'message_list'

    def get_queryset(self):
        """Get message trash list"""

        current_user = auth.get_user(self.request)
        return Message.objects.trash_for(current_user)


class TrashListFilteredView(ListView):
    "Message list filterd by title, location"

    model = Message
    template_name = 'message/trash/trash.html'
    context_object_name = 'filtered_message_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Message.objects.trash_for.filter(
            Q(sender__first_name__icontains=query) |
            Q(sender__last_name__icontains=query) |
            Q(recipient__first_name__icontains=query) |
            Q(recipient__last_name__icontains=query) |
            Q(message__icontains=query) |
            Q(subject__icontains=query)
        )
        return object_list


class TrashMessageDetailView(DetailView):
    "Message detail view"

    model = Message
    template_name = 'message/trash/detail.html'
    context_object_name = 'message'


def message_restore(request, pk):
    "Place a message in the trash"

    message = Message.objects.get(pk=pk)
    current_user = auth.get_user(request)

    if message.sender == current_user and message.recipient == current_user:
        message.sender_restore()
        message.recipient_restore()
    elif message.sender == current_user:
        message.sender_restore()
    else:
        message.recipient_restore()

    return redirect(reverse_lazy("message:message-trash"))
