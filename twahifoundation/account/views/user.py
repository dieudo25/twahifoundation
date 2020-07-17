from django.contrib.auth import get_user_model
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    "User profile view"

    """     model = get_user_model() """
    template_name = 'account/profile.html'
