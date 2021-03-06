from django.contrib.auth import get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy, reverse

from notifications.models import Notification

from account.permissions.group import group_required, GroupRequiredMixin
from blog.forms.post import (
    PostCreateUpdateForm, 
    PageCreateUpdateForm,
    PostCreateFormFR,
    PostCreateFormEN,
    PostUpdateFormLN,
)
from blog.models.post import Post
from blog.models.category import Category


# Post

class PostListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Post list view"

    model = Post
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'blog/post/list.html'
    context_object_name = 'post_list'
    queryset = Post.objects.filter(
        category__name="Post").order_by('-created_on')
    paginate_by = 10
    ordering = '-created_on'


class PostListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Post list filterd by title, location"

    model = Post
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'blog/post/list.html'
    context_object_name = 'filtered_post_list'
    paginate_by = 10
    ordering = '-created_on'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Post.objects.filter(category__name="Post").filter(
            Q(title__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        )
        return object_list


class PostDetailView(LoginRequiredMixin, GroupRequiredMixin, DetailView):
    "Post detail view"

    model = Post
    group_required = [u'Administrator',
                      u'Project manager', u'Editor', u'Member']
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'

    def get_object(self):
        instance = super().get_object()

        try:
            notice_id = self.kwargs['notice_pk']
            notice = Notification.objects.get(id=notice_id)

            if notice.unread:
                notice.delete()

            return instance
        except:
            return instance


class PostUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Post update view"

    model = Post
    group_required = [u'Administrator', u'Project manager', u'Editor']
    template_name = 'blog/post/update.html'
    context_object_name = 'post'
    form_class = PostUpdateFormLN

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("blog:post-detail", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        current_user = get_user(self.request)
        form.instance.updated_by = current_user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Post Delete View"

    model = Post
    group_required = [u'Administrator', u'Project manager', u'Editor']
    template_name = 'blog/post/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:post-list')


class PostCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Post create view"

    model = Post
    group_required = [u'Administrator', u'Project manager', u'Editor']
    template_name = 'blog/post/create.html'
    form_class = PostCreateUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cookie_language = self.request.COOKIES.get('django_language')

        if cookie_language == 'en':
            context["form_ln"] =  PostCreateFormEN
        else:
            context["form_ln"] =  PostCreateFormFR
        return context
    

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("blog:post-detail", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        form.instance.category = Category.objects.get(
            name="Post")
        form.instance.user = self.request.user
        return super().form_valid(form)

# Static page


class PageListView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Page list view"

    model = Post
    group_required = [u'Administrator',
                      u'Project Manager', u'Editor', u'Member']
    template_name = 'blog/page/list.html'
    context_object_name = 'page_list'
    queryset = Post.objects.filter(
        category__name="Page").order_by('-created_on')
    paginate_by = 10


class PageListFilteredView(LoginRequiredMixin, GroupRequiredMixin, ListView):
    "Page list filterd by title, author name"

    model = Post
    group_required = [u'Administrator',
                      u'Project Manager', u'Editor', u'Member']
    template_name = 'blog/page/list.html'
    context_object_name = 'filtered_page_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Post.objects.filter(category__name="Page").filter(
            Q(title__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        )
        return object_list


class PageCreateView(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    "Page create view"

    model = Post
    group_required = [u'Administrator', ]
    template_name = 'blog/page/create.html'
    form_class = PageCreateUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cookie_language = self.request.COOKIES.get('django_language')

        if cookie_language == 'en':
            context["form_ln"] =  PostCreateFormEN
        else:
            context["form_ln"] =  PostCreateFormFR
        return context

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("blog:page-detail", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        form.instance.category = Category.objects.get(
            name="Page")
        form.instance.user = self.request.user
        if not form.instance.image:
            form.instance.image = 'https://urbandojo.com/wp-content/uploads/2017/04/default-image.jpg'
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    "Page update view"

    model = Post
    group_required = [u'Administrator', u'Project manager']
    template_name = 'blog/page/update.html'
    context_object_name = 'post'
    form_class = PostUpdateFormLN

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("blog:page-detail", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        current_user = get_user(self.request)
        form.instance.updated_by = current_user
        return super().form_valid(form)


class PageDeleteView(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    "Page Delete View"

    model = Post
    group_required = [u'Administrator', ]
    template_name = 'blog/page/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:page-list')


@group_required('Administrator', 'Project manager')
def post_draft_publish(request, slug):
    "Change the status of a post"

    post = Post.objects.get(slug=slug)
    post.status_toggle()
    return redirect(reverse("blog:post-detail", kwargs={"slug": post.slug}))
