from datetime import datetime
from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from notifications.models import Notification

from account.permissions.group import group_required, GroupRequiredMixin
from project.models.project import Project
from project.forms.project import (
    ProjectCreateUpdateForm,
    ProjectCreateFormEN,
    ProjectCreateFormFR,
    ProjectUpdateForm,
)


class ProjectListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Project list view"

    model = Project
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'project/project/list.html'
    context_object_name = 'project_list'
    paginate_by = 10

    def get_queryset(self):
        object_list = Project.objects.exclude(is_deleted=True)
        return object_list


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
        ).exclude(is_deleted=True)
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
            notifications = Notification.objects.filter(
                action_object_object_id=instance.pk, recipient=current_user.pk)
        except Notification.DoesNotExist:
            return instance

        for notice in notifications:
            if notice.unread:
                notice.delete()

        return instance


class ProjectUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Project update view"

    model = Project
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/project/update.html'
    context_object_name = 'project'
    form_class = ProjectUpdateForm


class ProjectDeleteView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Project Delete View"

    model = Project
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/project/delete.html'
    context_object_name = 'project'


class ProjectCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Project create view"

    model = Project
    group_required = [u'Administrator', u'Project manager']
    template_name = 'project/project/create.html'
    form_class = ProjectCreateUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cookie_language = self.request.COOKIES.get('django_language')

        if cookie_language == 'en':
            context["form_ln"] =  ProjectCreateFormEN
        else:
            context["form_ln"] =  ProjectCreateFormFR
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@group_required('Administrator', 'Project manager')
def open_close_project(request, slug):
    "Place a message in the trash"

    project = get_object_or_404(Project, slug=slug)

    if not project.date_ended:
        project.date_ended = datetime.now()
        project.is_closed = True
    else:
        project.date_ended = None
        project.is_closed = False
    project.save()

    return redirect(reverse_lazy("project:project-detail", kwargs={"slug": project.slug}))


@group_required('Administrator', 'Project manager')
def project_draft_publish(request, slug):
    "Change the status of a project"

    project = get_object_or_404(Project, slug=slug)
    project.status_toggle()
    return redirect(reverse_lazy("project:project-detail", kwargs={"slug": project.slug}))


@group_required('Administrator', 'Project manager')
def delete_restore(request, slug):
    "Change the status of a project"

    project = get_object_or_404(Project, slug=slug)
    project.delete_toggle()
    return redirect(reverse_lazy("project:project-list"))
