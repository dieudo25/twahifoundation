from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from project.models.project import Project
from project.forms.project import ProjectCreateUpdateForm


class ProjectListView(ListView):
    "Project list view"

    model = Project
    template_name = 'project/project/list.html'
    context_object_name = 'project_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['project_number'] = Project.objects.all().count()
        return context


class ProjectListFilteredView(ListView):
    "Project list filterd by title, location"

    model = Project
    template_name = 'project/project/list.html'
    context_object_name = 'filtered_project_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Project.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


class ProjectDetailView(DetailView):
    "Project detail view"

    model = Project
    template_name = 'project/project/detail.html'
    context_object_name = 'project'


class ProjectUpdateView(UpdateView):
    "Project update view"

    model = Project
    template_name = 'project/project/update.html'
    context_object_name = 'project'
    form_class = ProjectCreateUpdateForm


class ProjectDeleteView(DeleteView):
    "Project Delete View"

    model = Project
    template_name = 'project/project/delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('project:project-list')


class ProjectCreateView(CreateView):
    "Project create view"

    model = Project
    template_name = 'project/project/create.html'
    form_class = ProjectCreateUpdateForm
