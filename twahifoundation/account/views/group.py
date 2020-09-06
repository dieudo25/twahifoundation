from django.db.models import Q
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import PermissionRequiredMixin


class GroupListView(PermissionRequiredMixin, ListView):
    "Group list view"

    model = Group
    permission_required = 'account.view.group'
    template_name = 'account/group/list.html'
    context_object_name = 'group_list'


class GroupListFilteredView(PermissionRequiredMixin, ListView):
    "Group list filterd by groupname, lastname or firstname"

    model = Group
    permission_required = 'account.view.group'
    template_name = 'account/group/list.html'
    context_object_name = 'filtered_group_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Group.objects.filter(
            Q(groupname__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
        return object_list


class GroupDetailView(DetailView):
    "Group detail view"

    model = Group
    template_name = 'account/group/detail.html'
    context_object_name = 'group'
