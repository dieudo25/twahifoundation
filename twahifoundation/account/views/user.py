from django.contrib.auth import get_user_model
from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from account.forms.user import UserCreateForm
from account.models.user import User


class UserListView(ListView):
    "User list view"

    model = get_user_model()
    template_name = 'account/user/list.html'
    context_object_name = 'user_list'


class UserListFilteredView(ListView):
    "User list filterd by username, lastname or firstname"

    model = get_user_model()
    template_name = 'account/user/list.html'
    context_object_name = 'filtered_user_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
        return object_list


class UserDetailView(DetailView):
    "User detail view"

    model = get_user_model()
    template_name = 'account/user/detail.html'
    context_object_name = 'user_profile'


class UserUpdateView(UpdateView):
    "User update view"

    model = get_user_model()
    template_name = 'account/user/update.html'
    fields = ['first_name',
              'last_name',
              'email',
              'language',
              'avatar', ]


class UserDeleteView(DeleteView):
    "User Delete View"

    model = get_user_model()
    template_name = 'account/user/delete.html'
    context_object_name = 'user_profile'
    success_url = reverse_lazy('account:user-list')


class UserCreateView(CreateView):
    "User create view"

    model = get_user_model()
    form_class = UserCreateForm
    template_name = 'account/user/create.html'
