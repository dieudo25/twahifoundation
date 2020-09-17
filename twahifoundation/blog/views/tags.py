from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from account.permissions.group import GroupRequiredMixin
from blog.models.tags import Tags
from blog.forms.tags import TagsCreateUpdateForm


class TagsListView(ListView):
    "Tags list view"

    model = Tags
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'blog/tags/list.html'
    context_object_name = 'tags_list'
    paginate_by = 10


class TagsListFilteredView(ListView):
    "Tags list filterd by title, location"

    model = Tags
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'blog/tags/list.html'
    context_object_name = 'filtered_tags_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Tags.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


class TagsUpdateView(UpdateView):
    "Tags update view"

    model = Tags
    group_required = [u'Administrator', u'Project manager', u'Editor']
    template_name = 'blog/tags/update.html'
    context_object_name = 'tags'
    form_class = TagsCreateUpdateForm
    success_url = reverse_lazy('blog:tags-list')


class TagsDeleteView(DeleteView):
    "Tags Delete View"

    model = Tags
    group_required = [u'Administrator', u'Project manager', u'Editor']
    template_name = 'blog/tags/delete.html'
    context_object_name = 'tags'
    success_url = reverse_lazy('blog:tags-list')


class TagsCreateView(CreateView):
    "Tags create view"

    model = Tags
    group_required = [u'Administrator', u'Project manager', u'Editor']
    template_name = 'blog/tags/create.html'
    form_class = TagsCreateUpdateForm
    success_url = reverse_lazy('blog:tags-list')
