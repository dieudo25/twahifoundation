from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy

from notifications.models import Notification

from account.permissions.group import group_required, GroupRequiredMixin
from message.models.message import Message
from message.forms.message import MessageCreateUpdateForm
""" from portal.views.views import mark_as_read """


class InboxListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Message list view"

    model = Message
    group_required = [u'Administrator', u'Member']
    template_name = 'message/inbox/list.html'
    context_object_name = 'inbox_list'
    paginate_by = 10

    def get_queryset(self):
        """Get Message inbox list"""

        current_user = get_user(self.request)
        return Message.objects.inbox_for(current_user)


class InboxListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Message list filterd by title, location"

    model = Message
    group_required = [u'Administrator', u'Member']
    template_name = 'message/inbox/inbox.html'
    context_object_name = 'filtered_inbox_list'
    paginate_by = 10

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


class InboxMessageDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Message detail view"

    model = Message
    group_required = [u'Administrator', u'Member']
    template_name = 'message/inbox/detail.html'
    context_object_name = 'message'

    def get_object(self):
        instance = super().get_object()

        message_id = self.kwargs['pk']
        message = get_object_or_404(Message, pk=message_id)
        message.read()

        try:
            notice_id = self.kwargs['notice_pk']
            notice = Notification.objects.get(id=notice_id)

            if notice.unread:
                notice.mark_as_read()

            return instance
        except:
            return instance


@group_required('Administrator', 'Member')
def inbox_to_trash(request, pk):
    "Place a message in the trash"

    message = Message.objects.get(pk=pk)
    message.recipient_delete()
    return redirect(reverse_lazy("message:inbox"))
