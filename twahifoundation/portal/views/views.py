from django.views.generic import TemplateView


class Home(TemplateView):
    "Portal Home page"

    template_name = 'portal/home.html'
