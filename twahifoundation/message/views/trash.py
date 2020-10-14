from django.conf import settings
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy

from account.permissions.group import group_required, GroupRequiredMixin
from message.models.message import Message
from message.forms.message import MessageCreateUpdateForm


class TrashListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Message list view"

    model = Message
    group_required = [u'Administrator', u'Member']
    template_name = 'message/trash/list.html'
    context_object_name = 'trash_list'
    paginate_by = 10
    ordering = ['-sent_at']

    def get_queryset(self):
        """Get message trash list"""

        current_user = get_user(self.request)
        return Message.objects.trash_for(current_user)


class TrashListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Message list filterd by title, location"

    model = Message
    group_required = [u'Administrator', u'Member']
    template_name = 'message/trash/list.html'
    context_object_name = 'filtered_trash_list'
    paginate_by = 10
    ordering = ['-sent_at']

    def get_queryset(self):
        current_user = get_user(self.request)
        query = self.request.GET.get('search')
        object_list = Message.objects.filter(
            Q(recipient=current_user) |
            Q(recipient_deleted_at__isnull=False) |
            Q(sender=current_user) |
            Q(sender_deleted_at__isnull=False)
        ).filter(
            Q(sender__first_name__icontains=query) |
            Q(sender__last_name__icontains=query) |
            Q(recipient__first_name__icontains=query) |
            Q(recipient__last_name__icontains=query) |
            Q(subject__icontains=query)
        )
        return object_list


class TrashMessageDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Message detail view"

    model = Message
    group_required = [u'Administrator', u'Member']
    template_name = 'message/trash/detail.html'
    context_object_name = 'message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["MEDIA_URL"] = settings.MEDIA_URL
        return context


@group_required('Administrator', 'Member')
def message_restore(request, pk):
    "Place a message in the trash"

    message = Message.objects.get(pk=pk)
    current_user = get_user(request)

    if message.sender == current_user and message.recipient == current_user:
        message.sender_restore()
        message.recipient_restore()
    elif message.sender == current_user:
        message.sender_restore()
    else:
        message.recipient_restore()

    return redirect(reverse_lazy("message:trash"))


@group_required('Administrator', 'Member')
def message_delete_once(request, pk):
    "Place a message in the trash"

    message = Message.objects.get(pk=pk)
    current_user = get_user(request)

    if message.sender == current_user:
        message.sender_deleted_once()
    else:
        message.recipient_deleted_once()

    return redirect(reverse_lazy("message:trash"))
