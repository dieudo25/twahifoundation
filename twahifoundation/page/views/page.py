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
        context["page_project_list"] = Project.objects.all().order_by(
            '-date_created')[:3]
        context["news_list"] = Post.objects.filter(status='Published', category__name="Post").order_by(
            '-created_on')[:3]
        context["page_event_list"] = Event.objects.filter(event_type="FundRaising").order_by(
            '-date_created')[:2]

        cookie = self.request.COOKIES.get('cookie_consent_user_accepted')

        context['cookie'] = cookie
        return context


class AboutView(TemplateView):
    "About page"

    template_name = "page/static_page/page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = Post.objects.get(title="About us")
        return context


class LegalMentionsView(TemplateView):
    "LegalMentions page"

    template_name = "page/static_page/page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = Post.objects.get(title="Legal mentions")
        return context


class AttributionsView(TemplateView):
    "Attributions page"

    template_name = "page/static_page/page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page"] = Post.objects.get(title="Attributions")
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
    paginate_by = 5
    template_name = 'page/event/list.html'
    context_object_name = 'page_event_list'
    queryset = Event.objects.filter(event_type="FundRaising")


class ProjectListView(ListView):
    "Event list view"

    model = Project
    paginate_by = 5
    template_name = 'page/project/list.html'
    context_object_name = 'page_project_list'


class NewsListView(ListView):
    "Event list view"

    model = Post
    paginate_by = 5
    template_name = 'page/news/list.html'
    context_object_name = 'news_list'
    queryset = Post.objects.filter(status='Published', category__name="Post")


class EventDetailView(DetailView):
    "Event detail view"

    model = Event
    template_name = 'page/event/detail.html'
    context_object_name = 'event'


class ProjectDetailView(DetailView):
    "Project detail view"

    model = Project
    template_name = 'page/project/detail.html'
    context_object_name = 'project'


class NewsDetailView(DetailView):
    "Post detail view"

    model = Post
    template_name = 'page/news/detail.html'
    context_object_name = 'post'
