from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from account.forms.user import UserCreateForm, UserUpdateForm, UserGroupUpdateForm
from account.models.user import User
from account.permissions.group import GroupRequiredMixin


class UserListView(LoginRequiredMixin, ListView):
    "User list view"

    model = get_user_model()
    template_name = 'account/user/list.html'
    context_object_name = 'user_list'
    paginate_by = 10


class UserListFilteredView(LoginRequiredMixin, ListView):
    "User list filterd by username, lastname or firstname"

    model = get_user_model()
    template_name = 'account/user/list.html'
    context_object_name = 'filtered_user_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
        return object_list


class UserDetailView(LoginRequiredMixin, DetailView):
    "User detail view"

    model = get_user_model()
    template_name = 'account/user/detail.html'
    context_object_name = 'user_profile'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    "User update view"

    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'account/user/update.html'


class UserDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "User Delete View"

    model = get_user_model()
    group_required = [u'Administrator', ]
    template_name = 'account/user/delete.html'
    context_object_name = 'user_profile'
    success_url = reverse_lazy('user-list')


class UserCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "User create view"

    model = get_user_model()
    group_required = [u'Administrator', u'President']
    form_class = UserCreateForm
    template_name = 'account/user/create.html'


class UserPasswordChangeView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "User update view"

    model = get_user_model()
    group_required = [u'Member', ]
    form_class = PasswordChangeForm
    template_name = 'account/auth/password_change_form.html'

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("user-detail", kwargs={"slug": self.object.slug})


class UserUpdateGroupsView(LoginRequiredMixin, UpdateView):
    "User detail view"

    model = get_user_model()
    template_name = 'account/user/update_group.html'
    context_object_name = 'user_profile'
    form_class = UserGroupUpdateForm


def user_statut_toggle(request, slug):
    "Change the status of the user"

    user = get_object_or_404(get_user_model(), slug=slug)

    if user.is_active:
        user.activate_deactivate()
        user.groups.clear()
        return redirect(reverse_lazy("user-detail", kwargs={"slug": user.slug}))
    else:
        user.activate_deactivate()
        return redirect(reverse_lazy("user-update-group", kwargs={"slug": user.slug}))