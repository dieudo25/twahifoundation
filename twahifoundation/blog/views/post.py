from django.db.models import Q
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

from blog.models.post import Post
from blog.models.category import Category

from blog.forms.post import PostCreateUpdateForm, PageCreateUpdateForm


# Post

class PostListView(ListView):
    "Post list view"

    model = Post
    template_name = 'blog/post/list.html'
    context_object_name = 'post_list'
    queryset = Post.objects.filter(
        category__name="Post").order_by('-created_on')


class PostListFilteredView(ListView):
    "Post list filterd by title, location"

    model = Post
    template_name = 'blog/post/list.html'
    context_object_name = 'filtered_post_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Post.objects.filter(category__name="Post").filter(
            Q(title__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
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

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("blog:post-detail", kwargs={"slug": self.object.slug})


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

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("blog:post-detail", kwargs={"slug": self.object.slug})

    def form_valid(self, PostCreateUpdateForm):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        PostCreateUpdateForm.instance.category = Category.objects.get(
            name="Post")
        PostCreateUpdateForm.instance.user = self.request.user
        return super().form_valid(PostCreateUpdateForm)

# Static page


class PageListView(ListView):
    "Page list view"

    model = Post
    template_name = 'blog/page/list.html'
    context_object_name = 'page_list'
    queryset = Post.objects.filter(
        category__name="Page").order_by('-created_on')


class PageListFilteredView(ListView):
    "Page list filterd by title, location"

    model = Post
    template_name = 'blog/page/list.html'
    context_object_name = 'filtered_page_list'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Post.objects.filter(category__name="Page").filter(
            Q(title__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        )
        return object_list


class PageCreateView(CreateView):
    "Page create view"

    model = Post
    template_name = 'blog/page/create.html'
    form_class = PageCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("blog:page-detail", kwargs={"slug": self.object.slug})

    def form_valid(self, PageCreateUpdateForm):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # perform a action here
        PageCreateUpdateForm.instance.category = Category.objects.get(
            name="Page")
        PageCreateUpdateForm.instance.user = self.request.user
        if not PageCreateUpdateForm.instance.image:
            PageCreateUpdateForm.instance.image = 'https://urbandojo.com/wp-content/uploads/2017/04/default-image.jpg'
        return super().form_valid(PageCreateUpdateForm)


class PageUpdateView(UpdateView):
    "Page update view"

    model = Post
    template_name = 'blog/page/update.html'
    context_object_name = 'post'
    form_class = PageCreateUpdateForm

    def get_success_url(self):
        "Get the absolute url of the object"
        return reverse_lazy("blog:page-detail", kwargs={"slug": self.object.slug})


class PageDeleteView(DeleteView):
    "Page Delete View"

    model = Post
    template_name = 'blog/page/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:page-list')
