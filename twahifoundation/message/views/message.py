from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from django_messages.models import Message

from message.forms.message import MessageCreateUpdateForm


class MessageSendListView(ListView):
    "Message list view"

    model = Message
    template_name = 'message/message/list.html'
    context_object_name = 'message_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['message_number'] = Message.objects.all().count()
        return context

    def get_queryset(self):
        """Returns Polls that were created today"""

        return Message.objects.outbox_for(recipient=self.request.user)


class MessageSendListFilteredView(ListView):
    "Message list filterd by title, location"

    model = Message
    template_name = 'message/message/list.html'
    context_object_name = 'filtered_message_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Message.objects.outbox_for.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query) |
            Q(user_first_name__icontains=query)
        )
        return object_list


class MessageReceivedListView(ListView):
    "Message list view"

    model = Message
    template_name = 'message/message/inbox.html'
    context_object_name = 'message_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['message_number'] = Message.objects.all().count()
        return context

    def get_queryset(self):
        """Returns Polls that were created today"""

        return Message.objects.inbox_for(self.request.user)


class MessageReceivedListFilteredView(ListView):
    "Message list filterd by title, location"

    model = Message
    template_name = 'message/message/inbox.html'
    context_object_name = 'filtered_message_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Message.objects.filter(
            Q(subject=query)
        )
        return object_list


class MessageDetailView(DetailView):
    "Message detail view"

    model = Message
    template_name = 'message/message/detail.html'
    context_object_name = 'message'


class MessageUpdateView(UpdateView):
    "Message update view"

    model = Message
    template_name = 'message/message/update.html'
    context_object_name = 'message'
    form_class = MessageCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("message:message-detail", kwargs={"pk": self.object.pk})


class MessageDeleteView(DeleteView):
    "Message Delete View"

    model = Message
    template_name = 'message/message/delete.html'
    context_object_name = 'message'
    success_url = reverse_lazy('message:message-list')


class MessageCreateView(CreateView):
    "Message create view"

    model = Message
    template_name = 'message/message/create.html'
    form_class = MessageCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("message:message-detail", kwargs={"slug": self.object.slug})
