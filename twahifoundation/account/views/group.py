from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import Group

from account.permissions.group import GroupRequiredMixin


class GroupListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Group list view"

    model = Group
    group_required = [u'Administrator', u'President']
    template_name = 'account/group/list.html'
    context_object_name = 'group_list'
    ordering = ['name']


class GroupListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Group list filterd by groupname, lastname or firstname"

    model = Group
    group_required = [u'Administrator', u'President']
    template_name = 'account/group/list.html'
    context_object_name = 'filtered_group_list'
    ordering = ['name']

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Group.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


class GroupDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Group detail view"

    model = Group
    group_required = [u'Administrator', u'President']
    template_name = 'account/group/detail.html'
    context_object_name = 'group'
