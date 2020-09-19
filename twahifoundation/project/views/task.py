from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from notifications.models import Notification
from notifications.signals import notify

from account.permissions.group import GroupRequiredMixin
from project.models.task import Task
from project.forms.task import TaskCreateUpdateForm


class TaskListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Task list view"

    model = Task
    group_required = [u'Administrator', u'Project manager', u'Member']
    template_name = 'project/task/list.html'
    context_object_name = 'task_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['task_number'] = Task.objects.all().count()
        context['todo_list'] = Task.objects.filter(state='TODO')
        context['pending_list'] = Task.objects.filter(state='PENDING')
        context['in_progress_list'] = Task.objects.filter(state='IN_PROGRESS')
        context['late_list'] = Task.objects.filter(state='LATE')
        context['done_list'] = Task.objects.filter(state='DONE')
        return context


class TaskListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Task list filterd by title, location"

    model = Task
    group_required = [u'Administrator', u'Project manager', u'Member']
    template_name = 'project/task/list.html'
    context_object_name = 'filtered_task_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Task.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


class TaskDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Task detail view"

    model = Task
    group_required = [u'Administrator', u'Project manager', u'Member']
    template_name = 'project/task/detail.html'
    context_object_name = 'task'

    def get_object(self):
        instance = super().get_object()

        try:
            notice_id = self.kwargs['notice_pk']
            notice = Notification.objects.get(id=notice_id)

            if notice.unread:
                notice.mark_as_read()

            return instance
        except:
            return instance


class TaskUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Task update view"

    model = Task
    group_required = [u'Administrator', u'Project manager', u'Member']
    template_name = 'project/task/update.html'
    context_object_name = 'task'
    form_class = TaskCreateUpdateForm


class TaskDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Task Delete View"

    model = Task
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/task/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('project:task-list')


class TaskCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Task create view"

    model = Task
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/task/create.html'
    form_class = TaskCreateUpdateForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        current_user = get_user(self.request)
        form.instance.created_by = current_user
        return super().form_valid(form)
