from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from notifications.models import Notification

from account.permissions.group import group_required, GroupRequiredMixin


class Home(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    "Portal Home page"

    group_required = [u'Administrator', u'Member']
    template_name = 'portal/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_user = get_user(self.request)
        context["notifications_unread"] = current_user.notifications.unread()
        return context


class NotificationList(LoginRequiredMixin, GroupRequiredMixin, TemplateView):

    group_required = [u'Administrator', u'Member']
    template_name = 'portal/notification/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_user = get_user(self.request)
        context["notifications_unread"] = current_user.notifications.unread()
        return context


@group_required('Administrateur', 'Member')
def mark_as_read(request, pk):

    notice = Notification.objects.get(id=pk)
    notice.delete()
    return redirect(reverse_lazy("portal:user-notifications"))


@group_required('Administrateur', 'Member')
def mark_all_as_read(request):

    current_user = get_user(request)
    notices = current_user.notifications.unread()
    notices.delete()
    return redirect(reverse_lazy("portal:user-notifications"))
