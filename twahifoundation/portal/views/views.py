from django.contrib.auth import get_user
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from notifications.models import Notification


class Home(TemplateView):
    "Portal Home page"

    template_name = 'portal/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_user = get_user(self.request)
        context["notifications_unread"] = current_user.notifications.unread()
        return context


class NotificationList(TemplateView):

    template_name = 'portal/notification/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_user = get_user(self.request)
        context["notifications_unread"] = current_user.notifications.unread()
        return context


def mark_as_read(request, pk):

    notice = Notification.objects.get(id=pk)
    notice.delete()
    return redirect(reverse_lazy("portal:user-notifications"))


def mark_all_as_read(request):

    current_user = get_user(request)
    notices = current_user.notifications.unread()
    notices.delete()
    return redirect(reverse_lazy("portal:user-notifications"))
