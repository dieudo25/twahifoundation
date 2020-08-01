from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from project.models.event import Event


class EventListView(ListView):
    "Event list view"

    model = Event
    template_name = 'project/event/list.html'
    event_number = Event.objects.all().count()

    if (event_number == 0):
        context_object_name = 'empty_table'
    else:
        context_object_name = 'event_list'


class EventListFilteredView(ListView):
    "Event list filterd by email, lastname or firstname"

    model = Event
    template_name = 'project/event/list.html'
    context_object_name = 'filtered_event_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Event.objects.filter(
            Q(title__icontains=query) |
            Q(location__icontains=query)
        )
        return object_list


""" class EventDetailView(DetailView):
    "Event detail view"

    model = Event
    template_name = 'project/event/detail.html'
    context_object_name = 'event'


class EventUpdateView(UpdateView):
    "Event update view"

    model = Event
    template_name = 'project/event/update.html'
    context_object_name = 'event'
    fields = [
        'name',
        'email',
        'phone_number',
        'address',
        'website',
        'is_partner',
    ]


class EventDeleteView(DeleteView):
    "Event Delete View"

    model = Event
    template_name = 'project/event/delete.html'
    context_object_name = 'event'
    success_url = reverse_lazy('project:event-list')


class EventCreateView(CreateView):
    "Event create view"

    model = Event
    template_name = 'project/event/create.html'
    fields = [
        'name',
        'email',
        'phone_number',
        'address',
        'website',
        'is_partner',
    ] """
