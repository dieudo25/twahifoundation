from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from django_blog_it.django_blog_it.models import Post

from blog.forms.post import PostCreateUpdateForm


class PostListView(ListView):
    "Post list view"

    model = Post
    template_name = 'blog/post/list.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['post_number'] = Post.objects.all().count()
        return context


class PostListFilteredView(ListView):
    "Post list filterd by title, location"

    model = Post
    template_name = 'blog/post/list.html'
    context_object_name = 'filtered_post_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Post.objects.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query) |
            Q(user_first_name__icontains=query)
        )
        return object_list


class PostDetailView(DetailView):
    "Post detail view"

    model = Post
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    "Post update view"

    model = Post
    template_name = 'blog/post/update.html'
    context_object_name = 'post'
    form_class = PostCreateUpdateForm


class PostDeleteView(DeleteView):
    "Post Delete View"

    model = Post
    template_name = 'blog/post/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:post-list')


class PostCreateView(CreateView):
    "Post create view"

    model = Post
    template_name = 'blog/post/create.html'
    form_class = PostCreateUpdateForm
