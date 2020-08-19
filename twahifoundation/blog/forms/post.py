from django import forms

from django_blog_it.django_blog_it.models import Post


class PostCreateUpdateForm(forms.ModelForm):
    """PostCreateForm custom made class"""

    class Meta:
        """Meta definition of PostCreateForm"""

        model = Post
        fields = [
            'title',
            'meta_description',
            'content',
            'category',
            'tags',
            'status',
            'keywords',
            'featured_image',
        ]
