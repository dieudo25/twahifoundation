from django.contrib.auth import get_user_model
from django.views.generic import DetailView, UpdateView


class ProfileView(DetailView):
    "User profile view"

    model = get_user_model()
    template_name = 'account/profile.html'
    context_object_name = 'user_profile'


class ProfileUpdateView(UpdateView):
    "User profile update view"

    model = get_user_model()
    template_name = 'account/profile_update.html'
    fields = ['first_name',
              'last_name',
              'email',
              'language']
