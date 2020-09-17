from django import forms

from blog.models.post import Post


class PostCreateUpdateForm(forms.ModelForm):
    """PostCreateForm custom made class"""

    class Meta:
        """Meta definition of PostCreateForm"""

        model = Post
        fields = [
            'title',
            'meta_description',
            'description',
            'content',
            'tags',
            'keywords',
            'image',
        ]


class PageCreateUpdateForm(forms.ModelForm):
    """PostCreateForm custom made class"""

    class Meta:
        """Meta definition of PostCreateForm"""

        model = Post
        fields = [
            'title',
            'meta_description',
            'content',
            'tags',
            'keywords',
        ]
