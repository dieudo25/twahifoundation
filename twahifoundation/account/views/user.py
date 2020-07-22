from django.contrib.auth import get_user_model
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from account.models.user import User


class UserListView(ListView):
    "User list view"

    model = get_user_model()
    template_name = 'account/user/list.html'
    context_object_name = 'user_list'


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
              'language']


class UserDeleteView(DeleteView):
    "User Delete View"

    model = get_user_model()
    template_name = 'account/user/delete.html'
    context_object_name = 'user_profile'
    success_url = reverse_lazy('account:user-list')


class UserCreateView(CreateView):
    ""

    model = get_user_model()
    template_name = 'account/user/create.html'
    fields = ['first_name',
              'last_name',
              'email',
              'language']
