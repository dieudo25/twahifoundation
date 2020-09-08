from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.urls import reverse_lazy

from blog.models.post import Post
from page.forms.contact import ContactForm
from project.models.project import Project
from project.models.event import Event


class HomeView(TemplateView):
    "Home page"

    template_name = 'page/home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_list"] = Project.objects.all().order_by(
            '-date_created')[:3]
        context["post_list"] = Post.objects.filter(status='Published', category__name="Post").order_by(
            '-created_on')[:3]
        context["event_list"] = Event.objects.filter(event_type="FundRaising").order_by(
            '-date_created')[:2]
        return context


class AboutView(TemplateView):
    "About page"

    template_name = "page/static_page/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = Post.objects.get(title="About")
        return context


class DonateView(TemplateView):
    "Donate view"

    template_name = "page/static_page/donate/donate.html"
    context_object_name = 'donate'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context


class ContactView(FormView):
    template_name = 'page/static_page/contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("page:contact-success")

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        from_email = form.cleaned_data.get('email')
        to_email = settings.EMAIL_HOST_USER
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        name = f'{ first_name } { last_name }'
        message = f'From { name } | { from_email } \n\n{ message }'
        send_mail(
            subject=subject.strip(),
            message=message,
            from_email=from_email,
            recipient_list=[to_email],
        )
        return super(ContactView, self).form_valid(form)


class ContactSuccessView(TemplateView):

    template_name = 'page/static_page/contact/success.html'


class FundRaisingEventListView(ListView):
    "Event list view"

    model = Event
    template_name = 'page/event/list.html'
    context_object_name = 'event_list'
    queryset = Event.objects.filter(event_type="FundRaising")
