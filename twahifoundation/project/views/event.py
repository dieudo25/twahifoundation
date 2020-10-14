from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy, reverse

from notifications.models import Notification

from account.permissions.group import group_required, GroupRequiredMixin
from project.models.event import Event
from project.forms.event import (
    EventCreateUpdateForm,
    EventCreateFormEN,
    EventCreateFormFR,
    EventUpdateFormLN,
)


class EventListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Event list view"

    model = Event
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'project/event/list.html'
    context_object_name = 'event_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['event_number'] = Event.objects.all().count()
        return context


class EventListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Event list filterd by title, location"

    model = Event
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'project/event/list.html'
    context_object_name = 'filtered_event_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Event.objects.filter(
            Q(title__icontains=query) |
            Q(location__icontains=query)
        )
        return object_list


class EventCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Event create view"

    model = Event
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/event/create.html'
    form_class = EventCreateUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cookie_language = self.request.COOKIES.get('django_language')

        if cookie_language == 'en':
            context["form_ln"] =  EventCreateFormEN
        else:
            context["form_ln"] =  EventCreateFormFR
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        current_user = get_user(self.request)
        form.instance.created_by = current_user
        return super().form_valid(form)


class EventDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Event detail view"

    model = Event
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'project/event/detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['users'] = Event.users
        return context

    def get_object(self):
        instance = super().get_object()

        try:
            notice_id = self.kwargs['notice_pk']
            notice = Notification.objects.get(id=notice_id)

            if notice.unread:
                notice.delete()

            return instance
        except:
            return instance


class EventUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Event update view"

    model = Event
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/event/update.html'
    context_object_name = 'event'
    form_class = EventUpdateFormLN


class EventDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Event Delete View"

    model = Event
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/event/delete.html'
    context_object_name = 'event'
    success_url = reverse_lazy('project:event-list')


@group_required('Administrator', 'Member')
def participate(request, slug):
    "Place a message in the trash"

    current_user = get_user(request)
    event = get_object_or_404(Event, slug=slug)

    if not current_user in event.users.all():
        event.users.add(current_user)
    else:
        event.users.remove(current_user)
    return redirect(reverse("project:event-detail", kwargs={"slug": event.slug}))


@group_required('Administrator', 'Project manager')
def event_draft_publish(request, slug):
    "Change the status of a event"

    event = get_object_or_404(Event, slug=slug)
    event.status_toggle()
    return redirect(reverse("project:event-detail", kwargs={"slug": event.slug}))
