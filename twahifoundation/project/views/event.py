from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from project.models.event import Event
from project.forms.event import EventCreateUpdateForm


class EventListView(ListView):
    "Event list view"

    model = Event
    template_name = 'project/event/list.html'
    context_object_name = 'event_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['event_number'] = Event.objects.all().count()
        return context


class EventListFilteredView(ListView):
    "Event list filterd by title, location"

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


class EventDetailView(DetailView):
    "Event detail view"

    model = Event
    template_name = 'project/event/detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['users'] = Event.users
        return context


class EventUpdateView(UpdateView):
    "Event update view"

    model = Event
    template_name = 'project/event/update.html'
    context_object_name = 'event'
    form_class = EventCreateUpdateForm


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
    form_class = EventCreateUpdateForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        form.instance.created_by = self.request.user
        return super().form_valid(form)
