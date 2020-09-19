from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from notifications.models import Notification

from account.permissions.group import group_required, GroupRequiredMixin
from project.models.project import Project
from project.forms.project import ProjectCreateUpdateForm


class ProjectListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Project list view"

    model = Project
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'project/project/list.html'
    context_object_name = 'project_list'
    paginate_by = 10


class ProjectListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Project list filterd by title, location"

    model = Project
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'project/project/list.html'
    context_object_name = 'filtered_project_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Project.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


class ProjectDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Project detail view"

    model = Project
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'project/project/detail.html'
    context_object_name = 'project'

    def get_object(self):
        instance = super().get_object()
        current_user = get_user(self.request)

        try:
            notice = Notification.objects.get(
                action_object_object_id=instance.pk, recipient=current_user.pk)
        except Notification.DoesNotExist:
            return instance

        if notice.unread:
            notice.mark_as_read()

        return instance


class ProjectUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Project update view"

    model = Project
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/project/update.html'
    context_object_name = 'project'
    form_class = ProjectCreateUpdateForm


class ProjectDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Project Delete View"

    model = Project
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/project/delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project:project-list')


class ProjectCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Project create view"

    model = Project
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/project/create.html'
    form_class = ProjectCreateUpdateForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        form.instance.created_by = self.request.user
        return super().form_valid(form)
