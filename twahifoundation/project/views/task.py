from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from project.models.task import Task
from project.forms.task import TaskCreateUpdateForm


class TaskListView(ListView):
    "Task list view"

    model = Task
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


class TaskListFilteredView(ListView):
    "Task list filterd by title, location"

    model = Task
    template_name = 'project/task/list.html'
    context_object_name = 'filtered_task_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Task.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


class TaskDetailView(DetailView):
    "Task detail view"

    model = Task
    template_name = 'project/task/detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    "Task update view"

    model = Task
    template_name = 'project/task/update.html'
    context_object_name = 'task'
    form_class = TaskCreateUpdateForm


class TaskDeleteView(DeleteView):
    "Task Delete View"

    model = Task
    template_name = 'project/task/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('project:task-list')


class TaskCreateView(CreateView):
    "Task create view"

    model = Task
    template_name = 'project/task/create.html'
    form_class = TaskCreateUpdateForm
